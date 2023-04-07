from pydozer.api import ApiClient
from tests.helper import api_client, dozer_server
from pydozer.ingest import IngestClient
from tests.helper import dozer_server, ingestion_client, arrow_ingestion_client
from pydozer.ingest_pb2 import IngestRequest
from pydozer.types_pb2 import Record, Value
import polars as pl
from pydozer.api import ApiClient
from pydozer.ingest import IngestClient
from tests.helper import dozer_server, ingestion_client, api_client
from pydozer.ingest_pb2 import IngestRequest
from pydozer.types_pb2 import Record, Value
from time import sleep

def test_api_count(api_client: ApiClient):
    res = api_client.count()
    assert res is not None
    assert res.count is not None


def test_api_describe(api_client: ApiClient):
    res = api_client.describe()
    assert res is not None
    assert len(res) > 3


def test_api_health(api_client: ApiClient):
    res = api_client.health()
    assert res is not None
    # SERVING = 1
    assert res.status == 1


def test_api_query(api_client: ApiClient):
    res = api_client.query()
    assert res is not None
    assert res.records is not None



def test_ingest(ingestion_client: IngestClient):
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


def test_ingest_df(ingestion_client):
    df = pl.read_parquet('tests/trips_small.parquet')
    res = ingestion_client.ingest_df('trips', df, seq_no=1)
    assert res is not None


def test_ingest_df_arrow(arrow_ingestion_client):
    df = pl.read_parquet('tests/trips_small.parquet')
    res = arrow_ingestion_client.ingest_df_arrow(
        'trips_arrow', df, batch_size=5, seq_no=1)
    assert res is not None




def test_ingest_query(ingestion_client: IngestClient, api_client: ApiClient):
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

    sleep(1)

    res = api_client.query()
    assert res is not None

    assert len(res.records) >= 1

    res = api_client.query({'$limit': 1})
    assert res is not None
    assert len(res.records) >= 1