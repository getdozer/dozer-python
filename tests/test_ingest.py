from tests.helper import dozer_server, ingestion_client
from dozer.ingest_pb2 import IngestRequest
from dozer.types_pb2 import Record, Value
import polars as pl


def test_ingest(dozer_server, ingestion_client):
    user = IngestRequest(
        schema_name="users",
        typ=0,
        old=None,
        new=Record(values=[Value(int_value=1),
                   Value(string_value="superman")]),
        seq_no=1
    )
    res = ingestion_client.ingest_raw(user)
    assert res is not None


def test_ingest_df(dozer_server, ingestion_client):
    df = pl.read_parquet('tests/trips_small.parquet')
    res = ingestion_client.ingest_df('trips', df, seq_no=1)
    assert res is not None


def test_ingest_df_arrow(dozer_server, ingestion_client):
    df = pl.read_parquet('tests/trips_small.parquet')
    res = ingestion_client.ingest_df_arrow('trips', df, batch_size=5, seq_no=1)
    assert res is not None
