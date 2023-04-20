import shutil
import subprocess

from time import sleep

from pydozer.auth import AuthClient
from pydozer.api import ApiClient
from pydozer.ingest import IngestClient

import pytest


DOZER_INGEST_URL = "0.0.0.0:10001"
DOZER_INGEST_ARROW_URL = "0.0.0.0:10005"
DOZER_API_URL = "0.0.0.0:10003"


# Run Dozer in background
@pytest.fixture(autouse=True, scope="session")
def dozer_server():
    which_dozer = shutil.which("dozer")
    p = subprocess.Popen([which_dozer, "-c", "tests/dozer-config.yaml"], stdout=subprocess.PIPE)
    while True:
        line = p.stdout.readline()
        if b'[api] Serving' in line:
            break
        if b'ERROR' in line:
            exit(1)
    sleep(1)
    yield
    p.terminate()
    p.kill()


@pytest.fixture
def api_client() -> ApiClient:
    master_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWNoZV91c2VyIiwic3ViIjoiYXBpQGRvemVyLmNvbSIsImV4cCI6MTY4MTI4NzcwNDAyNywiYWNjZXNzIjoiQWxsIn0.aD5L6XURIr3hrUp0LzfUQWKHairjK6DDkMlzvnVvzHA'

    client = AuthClient(token=master_token, url=DOZER_API_URL)

    restricted_token = client.get_auth_token()

    return ApiClient("users", url=DOZER_API_URL, token=restricted_token)


@pytest.fixture
def trips_client() -> ApiClient:
    return ApiClient("trips", url=DOZER_API_URL)


@pytest.fixture
def ingestion_client() -> IngestClient:
    return IngestClient(url=DOZER_INGEST_URL)


@pytest.fixture
def arrow_ingestion_client() -> IngestClient:
    return IngestClient(url=DOZER_INGEST_ARROW_URL)


