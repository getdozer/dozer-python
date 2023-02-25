from tests import constants
from common_pb2_grpc import CommonGrpcServiceStub
from common_pb2 import QueryRequest
import grpc


def test_api():
    channel = grpc.insecure_channel(constants.DOZER_API_URL)

    service = CommonGrpcServiceStub(channel=channel)
    res = service.count(QueryRequest(endpoint="trips"))
    assert res.count == 0
