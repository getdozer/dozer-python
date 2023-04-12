import json
import os
import grpc
from pydozer.helper import describe_services
from pydozer.auth_pb2_grpc import AuthGrpcServiceStub
import pydozer.auth_pb2 as auth__pb2


DOZER_API_URL = os.getenv("DOZER_API_URL", "0.0.0.0:50051")


class AuthClient:
    """Common Client for Dozer Authorization Service

    Args:
        token: A valid token to generate restricted tokens
        url (str, optional): Dozer gRPC URL. Defaults to Env variable DOZER_API_URL or `0.0.0.0:50051`.
    """
    def __init__(self, token, url=DOZER_API_URL, secure=False):

        self.metadata = [('authorization', f'Bearer {token}')]

        if secure:
            channel = grpc.secure_channel(url)
        else:
            channel = grpc.insecure_channel(url)

        self.channel = channel

        self.client = AuthGrpcServiceStub(channel)

    def describe(self) -> dict:
        """Describe the available gRPC services and methods

        Returns:
            dict: dictionary of available services and methods
        """

        return describe_services(self.channel)

    def get_auth_token(self, query: dict = None) -> auth__pb2.GetAuthTokenResponse:
        """Get a token for restricted access. Response is in the common format.

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
            GetAuthTokenResponse: {"token": token}
                token: A token with restricted access
        """

        if query is None or len(query) == 0:
            query_str = '"All"'
        else:
            data = {}
            for key, value in query.items():
                data[key] = value
            query_str = json.dumps(data)

        req = auth__pb2.GetAuthTokenRequest(access_filter=query_str)
        response = self.client.getAuthToken(req, metadata=self.metadata)
        return response.token

