from tests import helper
from dozer.common_pb2_grpc import CommonGrpcServiceStub
from dozer.common_pb2 import QueryRequest
import grpc


def test_api():
    proc = helper.dozer_background()

    channel = grpc.insecure_channel(helper.DOZER_API_URL)

    service = CommonGrpcServiceStub(channel=channel)
    res = service.count(QueryRequest(endpoint="trips"))
    assert res.count == 0

    proc.terminate()
