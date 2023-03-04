from tests import helper
from dozer.ingest_pb2_grpc import IngestServiceStub
from dozer.ingest_pb2 import IngestRequest
from dozer.types_pb2 import Record
import grpc


def test_ingest():
    proc = helper.dozer_background()
    channel = grpc.insecure_channel(helper.DOZER_INGEST_URL)

    service = IngestServiceStub(channel=channel)
    record = Record(values=[], version=0,)

    req = IngestRequest(schema_name="trips", typ=0, new=record)
    assert req is not None
    assert service is not None

    proc.terminate()
