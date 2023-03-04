# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dozer.ingest_pb2 as ingest__pb2


class IngestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ingest = channel.unary_unary(
            '/dozer.ingest.IngestService/ingest',
            request_serializer=ingest__pb2.IngestRequest.SerializeToString,
            response_deserializer=ingest__pb2.IngestResponse.FromString,
        )
        self.ingest_stream = channel.stream_unary(
            '/dozer.ingest.IngestService/ingest_stream',
            request_serializer=ingest__pb2.IngestRequest.SerializeToString,
            response_deserializer=ingest__pb2.IngestResponse.FromString,
        )
        self.ingest_arrow = channel.unary_unary(
            '/dozer.ingest.IngestService/ingest_arrow',
            request_serializer=ingest__pb2.IngestArrowRequest.SerializeToString,
            response_deserializer=ingest__pb2.IngestResponse.FromString,
        )
        self.ingest_arrow_stream = channel.stream_unary(
            '/dozer.ingest.IngestService/ingest_arrow_stream',
            request_serializer=ingest__pb2.IngestArrowRequest.SerializeToString,
            response_deserializer=ingest__pb2.IngestResponse.FromString,
        )


class IngestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ingest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ingest_stream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ingest_arrow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ingest_arrow_stream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IngestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ingest': grpc.unary_unary_rpc_method_handler(
            servicer.ingest,
            request_deserializer=ingest__pb2.IngestRequest.FromString,
            response_serializer=ingest__pb2.IngestResponse.SerializeToString,
        ),
        'ingest_stream': grpc.stream_unary_rpc_method_handler(
            servicer.ingest_stream,
            request_deserializer=ingest__pb2.IngestRequest.FromString,
            response_serializer=ingest__pb2.IngestResponse.SerializeToString,
        ),
        'ingest_arrow': grpc.unary_unary_rpc_method_handler(
            servicer.ingest_arrow,
            request_deserializer=ingest__pb2.IngestArrowRequest.FromString,
            response_serializer=ingest__pb2.IngestResponse.SerializeToString,
        ),
        'ingest_arrow_stream': grpc.stream_unary_rpc_method_handler(
            servicer.ingest_arrow_stream,
            request_deserializer=ingest__pb2.IngestArrowRequest.FromString,
            response_serializer=ingest__pb2.IngestResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'dozer.ingest.IngestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class IngestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ingest(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.ingest.IngestService/ingest',
                                             ingest__pb2.IngestRequest.SerializeToString,
                                             ingest__pb2.IngestResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ingest_stream(request_iterator,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dozer.ingest.IngestService/ingest_stream',
                                              ingest__pb2.IngestRequest.SerializeToString,
                                              ingest__pb2.IngestResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ingest_arrow(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dozer.ingest.IngestService/ingest_arrow',
                                             ingest__pb2.IngestArrowRequest.SerializeToString,
                                             ingest__pb2.IngestResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ingest_arrow_stream(request_iterator,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dozer.ingest.IngestService/ingest_arrow_stream',
                                              ingest__pb2.IngestArrowRequest.SerializeToString,
                                              ingest__pb2.IngestResponse.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
