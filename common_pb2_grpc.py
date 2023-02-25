# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
import types_pb2 as types__pb2


class CommonGrpcServiceStub(object):
    """*
    CommonGrpcService allows developers to query data from various endpoints.

    The service supports both Pull and Push queries. It provides methods to return metadata about the fields that can be used to construct the data types dynamically.

    This is preferred while working with libraries or in the case of dynamic scenarios and interpreted languages.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.count = channel.unary_unary(
                '/dozer.common.CommonGrpcService/count',
                request_serializer=common__pb2.QueryRequest.SerializeToString,
                response_deserializer=common__pb2.CountResponse.FromString,
                )
        self.query = channel.unary_unary(
                '/dozer.common.CommonGrpcService/query',
                request_serializer=common__pb2.QueryRequest.SerializeToString,
                response_deserializer=common__pb2.QueryResponse.FromString,
                )
        self.OnEvent = channel.unary_stream(
                '/dozer.common.CommonGrpcService/OnEvent',
                request_serializer=common__pb2.OnEventRequest.SerializeToString,
                response_deserializer=types__pb2.Operation.FromString,
                )
        self.getEndpoints = channel.unary_unary(
                '/dozer.common.CommonGrpcService/getEndpoints',
                request_serializer=common__pb2.GetEndpointsRequest.SerializeToString,
                response_deserializer=common__pb2.GetEndpointsResponse.FromString,
                )
        self.getFields = channel.unary_unary(
                '/dozer.common.CommonGrpcService/getFields',
                request_serializer=common__pb2.GetFieldsRequest.SerializeToString,
                response_deserializer=common__pb2.GetFieldsResponse.FromString,
                )


class CommonGrpcServiceServicer(object):
    """*
    CommonGrpcService allows developers to query data from various endpoints.

    The service supports both Pull and Push queries. It provides methods to return metadata about the fields that can be used to construct the data types dynamically.

    This is preferred while working with libraries or in the case of dynamic scenarios and interpreted languages.
    """

    def count(self, request, context):
        """*
        Counts the number of records satisfying the given query. See [Query](../query) for the query format.

        If no query is specified, total number of records will be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
        """*
        Performs query on an endpoint. See [Query](../query) for the query format.

        If no query is specified, the first 50 records will be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnEvent(self, request, context):
        """*
        Subscribes to the Dozer event stream, optionally applies a filter. See [Query](../query) for the filter format.

        This API is unstable and may change in the future.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEndpoints(self, request, context):
        """Gets all the endpoints Dozer is currently serving.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFields(self, request, context):
        """Gets the field description of an endpoint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommonGrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'count': grpc.unary_unary_rpc_method_handler(
                    servicer.count,
                    request_deserializer=common__pb2.QueryRequest.FromString,
                    response_serializer=common__pb2.CountResponse.SerializeToString,
            ),
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=common__pb2.QueryRequest.FromString,
                    response_serializer=common__pb2.QueryResponse.SerializeToString,
            ),
            'OnEvent': grpc.unary_stream_rpc_method_handler(
                    servicer.OnEvent,
                    request_deserializer=common__pb2.OnEventRequest.FromString,
                    response_serializer=types__pb2.Operation.SerializeToString,
            ),
            'getEndpoints': grpc.unary_unary_rpc_method_handler(
                    servicer.getEndpoints,
                    request_deserializer=common__pb2.GetEndpointsRequest.FromString,
                    response_serializer=common__pb2.GetEndpointsResponse.SerializeToString,
            ),
            'getFields': grpc.unary_unary_rpc_method_handler(
                    servicer.getFields,
                    request_deserializer=common__pb2.GetFieldsRequest.FromString,
                    response_serializer=common__pb2.GetFieldsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dozer.common.CommonGrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommonGrpcService(object):
    """*
    CommonGrpcService allows developers to query data from various endpoints.

    The service supports both Pull and Push queries. It provides methods to return metadata about the fields that can be used to construct the data types dynamically.

    This is preferred while working with libraries or in the case of dynamic scenarios and interpreted languages.
    """

    @staticmethod
    def count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.common.CommonGrpcService/count',
            common__pb2.QueryRequest.SerializeToString,
            common__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.common.CommonGrpcService/query',
            common__pb2.QueryRequest.SerializeToString,
            common__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dozer.common.CommonGrpcService/OnEvent',
            common__pb2.OnEventRequest.SerializeToString,
            types__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEndpoints(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.common.CommonGrpcService/getEndpoints',
            common__pb2.GetEndpointsRequest.SerializeToString,
            common__pb2.GetEndpointsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.common.CommonGrpcService/getFields',
            common__pb2.GetFieldsRequest.SerializeToString,
            common__pb2.GetFieldsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
