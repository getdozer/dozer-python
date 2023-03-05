import os
import grpc
from dozer.helper import describe_services
from dozer.health_pb2_grpc import HealthGrpcServiceStub
from dozer.common_pb2_grpc import CommonGrpcServiceStub
from dozer.common_pb2 import QueryRequest, OnEventRequest
from dozer.health_pb2 import HealthCheckRequest

DOZER_API_URL = os.getenv("DOZER_API_URL", "0.0.0.0:50051")


class ApiClient:
    def __init__(self, endpoint, url=DOZER_API_URL, secure=False):
        """Common API client for Dozer

        Args:
            endpoint (str): Endpoint to connect to. 
            url (str, optional): Dozer gRPC URL. Defaults to Env variable DOZER_API_URL or `0.0.0.0:50051`.
            secure (bool, optional): Intialize a secure channel. Defaults to False.
        """
        if secure:
            channel = grpc.secure_channel(url)
        else:
            channel = grpc.insecure_channel(url)
        self.endpoint = endpoint
        self.channel = channel
        self.client = CommonGrpcServiceStub(channel)

    def describe(self):
        """Prints out the available gRPC services and methods
        """
        return describe_services(self.channel)

    def health(self, service=None):
        """Checks the health of the Dozer Common Server
        """
        health_client = HealthGrpcServiceStub(self.channel)
        return health_client.healthCheck(HealthCheckRequest(service=service))

    def count(self, request={}):
        """Counts the number of records in Dozer cache. 

        Args:
            request (QueryRequest): Optionally accepts a filter 
            to count only a subset of records
        """
        _req = QueryRequest(endpoint=self.endpoint)
        for key, value in request.items():
            setattr(_req, key, value)
        return self.client.count(_req)

    def query(self, request={}):
        """Queries the Dozer cache for records. Response is in the common format.

        Args:
            request (QueryRequest): Optionally accepts a filter 
            to query only a subset of records
        """

        _req = QueryRequest(endpoint=self.endpoint)
        for key, value in request.items():
            setattr(_req, key, value)
        return self.client.query(_req)

    def on_event(self, request={}):
        """Subscribes to events from Dozer. 

        Args:
            request (OnEventRequest): Optionally accepts a filter
        """
        _req = OnEventRequest(endpoint=self.endpoint)
        for key, value in request.items():
            setattr(_req, key, value)
        return self.client.OnEvent(_req)
