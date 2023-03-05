from tests.helper import dozer_server, ingestion_client, api_client
from dozer.ingest_pb2 import IngestRequest
from dozer.types_pb2 import Record, Value


def test_ingest_query(dozer_server, ingestion_client, api_client):
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
