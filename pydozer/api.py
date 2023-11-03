import json
import os
import grpc
from pydozer.helper import describe_services
from pydozer.health_pb2_grpc import HealthGrpcServiceStub
from pydozer.common_pb2_grpc import CommonGrpcServiceStub
from pydozer.common_pb2 import QueryRequest, OnEventRequest, QueryResponse, CountResponse
from pydozer.health_pb2 import HealthCheckRequest, HealthCheckResponse
from pydozer.types_pb2 import EventFilter

DOZER_API_URL = os.getenv("DOZER_API_URL", "0.0.0.0:50051")


class ApiClient:
    """Common API client for Dozer

    Args:
        endpoint (str): Endpoint to connect to.
        url (str, optional): Dozer gRPC URL. Defaults to Env variable DOZER_API_URL or `0.0.0.0:50051`.
        secure (bool, optional): Intialize a secure channel. Defaults to False.
    """
    def __init__(self, endpoint, url=DOZER_API_URL, app_id=None, secure=False, token=None):

        self.metadata = []

        if app_id:
            self.metadata = [('x-dozer-app-id', app_id)]
        if token:
            self.metadata.insert(0, ('authorization', f'Bearer {token}'))

        if secure:
            channel = grpc.secure_channel(url, grpc.ssl_channel_credentials())
        else:
            channel = grpc.insecure_channel(url)
        self.endpoint = endpoint
        self.channel = channel
        self.client = CommonGrpcServiceStub(channel)

    def describe(self) -> dict:
        """Describe the available gRPC services and methods

        Returns:
            dict: dictionary of available services and methods
        """

        return describe_services(self.channel)

    def health(self, service: str = None) -> HealthCheckResponse:
        """Checks the health of the Dozer Common Server

        Args:
            service (str, optional): Name of the service. Defaults to None.
                                    Eg: `pydozer.generated.trips.Trips` for endpoint `trips`

        Returns:
            HealthCheckResponse: _description_
        """

        health_client = HealthGrpcServiceStub(self.channel)
        return health_client.healthCheck(HealthCheckRequest(service=service), metadata=self.metadata)

    def count(self, query: QueryRequest = {}) -> CountResponse:
        """Counts the number of records in Dozer cache.

        Args:
            query (dict, optional): Accepts a filter
            to query only a subset of records. 
            Keys could be 
                `$filter`: `dict` eg: `{"name": "John"}` or `{"id": { "$gt": 1}}`  
                `$limit`:  `int`
                `$skip`: `int`,
                '$after`: `int`, cursor to start from. `$skip` and `$after` cannot be used in the same query
                `$order_by`: `dict` eg: `{"name": "asc"}` or `{"id": "desc"}`
            Defaults to {}.

        Returns:
            CountResponse: count of records
        """

        req = self.get_query_request(query)
        return self.client.count(req, metadata=self.metadata)

    def query(self, query: dict = {}) -> QueryResponse:
        """Queries the Dozer cache for records. Response is in the common format.

        Args:
            query (dict, optional): Accepts a filter
            to query only a subset of records. 
            Keys could be 
                `$filter`: `dict` eg: `{"name": "John"}` or `{"id": { "$gt": 1}}`  
                `$limit`:  `int`
                `$skip`: `int`,
                '$after`: `int`, cursor to start from. `$skip` and `$after` cannot be used in the same query
                `$order_by`: `dict` eg: `{"name": "asc"}` or `{"id": "desc"}`
            Defaults to {}.

        Returns:
            QueryResponse: {"fields": fields, "records": records}
                fields: list of field definitions
                records: list of records
        """

        req = self.get_query_request(query)

        return self.client.query(req, metadata=self.metadata)

    def on_event(self, request={}):
        """Subscribes to events from Dozer.

        Args:
            request (OnEventRequest): Optionally accepts a filter
        """
        _req = OnEventRequest(endpoints={
            self.endpoint: EventFilter()
        })
        for key, value in request.items():
            setattr(_req, key, value)

        return self.client.OnEvent(_req, metadata=self.metadata)

    def get_query_request(self, query: dict = {}) -> QueryRequest:
        """Returns a QueryRequest object
        Args:
            query (dict, optional): Accepts a filter
            to query only a subset of records. 
            Keys could be 
                `$filter`: `dict` eg: `{"name": "John"}` or `{"id": { "$gt": 1}}`  
                `$limit`:  `int`
                `$skip`: `int`,
                '$after`: `int`, cursor to start from. `$skip` and `$after` cannot be used in the same query
                `$order_by`: `dict` eg: `{"name": "asc"}` or `{"id": "desc"}`
            Defaults to {}.
        Returns:
            QueryRequest: QueryRequest object
        """

        if query is None or len(query) == 0:
            query = {}

        data = {}
        for key, value in query.items():
            data[key] = value
        query_str = json.dumps(data)

        return QueryRequest(endpoint=self.endpoint, query=query_str)
