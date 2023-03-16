import shutil
import subprocess

from time import sleep

from dozer.api import ApiClient
from dozer.ingest import IngestClient
import pytest


DOZER_INGEST_URL = "0.0.0.0:7001"
DOZER_INGEST_ARROW_URL = "0.0.0.0:7005"
DOZER_API_URL = "0.0.0.0:7003"


# Run Dozer in background
@pytest.fixture(autouse=True, scope="session")
def dozer_server():
    which_dozer = shutil.which("dozer")
    p = subprocess.Popen([which_dozer, "-c", "tests/dozer-config.yaml"], stdout=subprocess.PIPE)
    while True:
        line = p.stdout.readline()
        if b'[api] Serving' in line:
            break
    sleep(0.1)
    yield
    p.terminate()
    p.kill()


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient("users", url=DOZER_API_URL)


@pytest.fixture
def trips_client() -> ApiClient:
    return ApiClient("trips", url=DOZER_API_URL)


@pytest.fixture
def ingestion_client() -> IngestClient:
    return IngestClient(url=DOZER_INGEST_URL)


@pytest.fixture
def arrow_ingestion_client() -> IngestClient:
    return IngestClient(url=DOZER_INGEST_ARROW_URL)


