from dozer.api import ApiClient
from tests.helper import api_client, dozer_server
from dozer.ingest import IngestClient
from tests.helper import dozer_server, ingestion_client, arrow_ingestion_client
from dozer.ingest_pb2 import IngestRequest
from dozer.types_pb2 import Record, Value
import polars as pl
from dozer.api import ApiClient
from dozer.ingest import IngestClient
from tests.helper import dozer_server, ingestion_client, api_client
from dozer.ingest_pb2 import IngestRequest
from dozer.types_pb2 import Record, Value

def test_api_count(dozer_server, api_client: ApiClient):
    res = api_client.count()
    assert res is not None
    assert res.count is not None


def test_api_describe(dozer_server, api_client: ApiClient):
    res = api_client.describe()
    assert res is not None
    assert len(res) > 3


def test_api_health(dozer_server, api_client: ApiClient):
    res = api_client.health()
    assert res is not None
    # SERVING = 1
    assert res.status == 1


def test_api_query(dozer_server, api_client: ApiClient):
    res = api_client.query()
    assert res is not None
    assert res.records is not None



def test_ingest(dozer_server, ingestion_client: IngestClient):
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


def test_ingest_df_arrow(dozer_server, arrow_ingestion_client):
    df = pl.read_parquet('tests/trips_small.parquet')
    res = arrow_ingestion_client.ingest_df_arrow(
        'trips_arrow', df, batch_size=5, seq_no=1)
    assert res is not None




def test_ingest_query(dozer_server, ingestion_client: IngestClient, api_client: ApiClient):
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

    res = api_client.query()
    assert res is not None

    assert len(res.records) >= 1

    res = api_client.query({'$limit': 1})
    assert res is not None
    assert len(res.records) >= 1