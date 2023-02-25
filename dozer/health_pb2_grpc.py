# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dozer.health_pb2 as health__pb2


class HealthGrpcServiceStub(object):
    """*
    The health service that checks health on services.
    *
    Get functions for health check

    [Reference] https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.healthCheck = channel.unary_unary(
            '/dozer.health.HealthGrpcService/healthCheck',
            request_serializer=health__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=health__pb2.HealthCheckResponse.FromString,
        )
        self.healthWatch = channel.unary_stream(
            '/dozer.health.HealthGrpcService/healthWatch',
            request_serializer=health__pb2.HealthCheckRequest.SerializeToString,
            response_deserializer=health__pb2.HealthCheckResponse.FromString,
        )


class HealthGrpcServiceServicer(object):
    """*
    The health service that checks health on services.
    *
    Get functions for health check

    [Reference] https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """

    def healthCheck(self, request, context):
        """Get function for health check
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def healthWatch(self, request, context):
        """Get function for health check watch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthGrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'healthCheck': grpc.unary_unary_rpc_method_handler(
            servicer.healthCheck,
            request_deserializer=health__pb2.HealthCheckRequest.FromString,
            response_serializer=health__pb2.HealthCheckResponse.SerializeToString,
        ),
        'healthWatch': grpc.unary_stream_rpc_method_handler(
            servicer.healthWatch,
            request_deserializer=health__pb2.HealthCheckRequest.FromString,
            response_serializer=health__pb2.HealthCheckResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'dozer.health.HealthGrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class HealthGrpcService(object):
    """*
    The health service that checks health on services.
    *
    Get functions for health check

    [Reference] https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """

    @staticmethod
    def healthCheck(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.health.HealthGrpcService/healthCheck',
                                             health__pb2.HealthCheckRequest.SerializeToString,
                                             health__pb2.HealthCheckResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def healthWatch(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dozer.health.HealthGrpcService/healthWatch',
                                              health__pb2.HealthCheckRequest.SerializeToString,
                                              health__pb2.HealthCheckResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
