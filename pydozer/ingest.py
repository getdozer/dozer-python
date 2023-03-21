import os
import grpc
from pydozer.helper import describe_services, map_arrow_df, map_record
from pydozer.ingest_pb2_grpc import IngestServiceStub
from pydozer.ingest_pb2 import IngestResponse
from tqdm import tqdm
import polars as pl

DOZER_INGEST_URL = os.getenv("DOZER_INGEST_URL", "0.0.0.0:8085")

BATCH_SIZE = 1000


class IngestClient:
    """Ingest client for Dozer

    Args:
        url (str, optional): Ingest Server URL. Defaults to DOZER_INGEST_URL or `0.0.0.0:8085`.
        secure (bool, optional): Intialize a secure channel. Defaults to False.
    """
    def __init__(self, url=DOZER_INGEST_URL, secure=False):
        channel = grpc.insecure_channel(url)
        if secure:
            channel = grpc.secure_channel(url)
        self.channel = channel
        self.ingestor = IngestServiceStub(channel)

    def describe(self) -> dict:
        """Prints out the available gRPC services and methods
        """
        return describe_services(self.channel)

    def ingest_raw(self, request) -> IngestResponse:
        """Ingest a record in Common Format into Dozer
           Eg: 
           ```
            user = IngestRequest(
                schema_name="users",
                typ=0,
                old=None,
                new=Record(values=[Value(int_value=1), Value(string_value="vivek")]),
                seq_no=1
            )
            ingestor.ingest(user)
           ```
        Args:
            request (IngestRequest): 
        """
        return self.ingestor.ingest(request)

    def ingest_raw_stream(self, generator) -> IngestResponse:
        """Ingest a stream in Common Format into Dozer
        Args:
            generator: Generator function that yields IngestRequest
        """
        return self.ingestor.ingest(generator)

    def ingest_df(self, schema_name, df, seq_no=1) -> IngestResponse:
        """Ingest a pandas dataframe into Dozer using ingest stream
        Args:
            schema_name (str): Schema name
            df (DataFrame): Pandas DataFrame
            seq_no (int, optional): Sequence number. Defaults to 1.
        """
        def get_messages(seq_no):
            for row in tqdm(df.iter_rows()):
                rec = map_record(schema_name, row, df.dtypes, seq_no)
                seq_no = seq_no + 1
                yield rec
        print("Ingesting via stream...")

        return self.ingestor.ingest_stream(get_messages(seq_no))

    def ingest_df_arrow(self, schema_name, df, batch_size=BATCH_SIZE, seq_no=1) -> IngestResponse:
        """Ingest a dataframe into Dozer in Arrow Format
        Args:
            schema_name (str): Schema name
            df (DataFrame): Pandas DataFrame
            batch_size (int, optional): Batch Size to be used for ingestion. 
                Defaults to BATCH_SIZE.
            seq_no (int, optional): Sequence number. Defaults to 1.
        """
        def get_messages(seq_no):
            partitions = df.with_row_count('__cnt').with_columns(
                pl.col('__cnt').apply(lambda i: int(i/batch_size))).partition_by('__cnt')

            with tqdm(total=df.shape[0]) as pbar:
                for par in partitions:
                    par = par.drop('__cnt')
                    msg = map_arrow_df(schema_name, par, seq_no)
                    seq_no = seq_no + batch_size
                    pbar.update(batch_size)
                    yield msg
                pbar.close()
        print("Ingesting via stream in Arrow Format...")

        return self.ingestor.ingest_arrow_stream(get_messages(seq_no))
