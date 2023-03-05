from time import sleep
import multiprocessing
import subprocess
from dozer.api import ApiClient
from dozer.ingest import IngestClient
import pytest

DOZER_INGEST_URL = "0.0.0.0:7001"
DOZER_INGEST_ARROW_URL = "0.0.0.0:7005"
DOZER_API_URL = "0.0.0.0:7003"

# Run Dozer in background


@pytest.fixture(autouse=True, scope="session")
def dozer_server():
    proc = multiprocessing.Process(target=server, args=())
    proc.start()
    yield
    proc.terminate()


@pytest.fixture
def api_client():
    return ApiClient("users", url=DOZER_API_URL)


@pytest.fixture
def trips_client():
    return ApiClient("trips", url=DOZER_API_URL)


@pytest.fixture
def ingestion_client():
    return IngestClient(url=DOZER_INGEST_URL)


@pytest.fixture
def arrow_ingestion_client():
    return IngestClient(url=DOZER_INGEST_ARROW_URL)


def server():
    subprocess.run(["dozer", "-c", "tests/dozer-config.yaml"])
