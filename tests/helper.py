import os
import multiprocessing
import subprocess
from time import sleep
DOZER_INGEST_URL = os.getenv("DOZER_INGEST_URL", "0.0.0.0:8089")
DOZER_API_URL = os.getenv("DOZER_API_URL", "0.0.0.0:50056")

# Run Dozer in background


def dozer_background():
    proc = multiprocessing.Process(target=dozer, args=())
    proc.start()
    sleep(1)
    return proc


def dozer():
    subprocess.run(["dozer", "-c", "tests/dozer-config.yaml"])
