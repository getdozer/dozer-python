<div align="center">
    <a target="_blank" href="https://getdozer.io/">
        <br><img src="https://dozer-assets.s3.ap-southeast-1.amazonaws.com/logo-blue.svg" width=40%><br>
    </a>
</div>

<p align="center">
    <br />
    <b>
    Connect any data source, combine them in real-time and instantly get low-latency gRPC and REST APIs.<br>
    ⚡ All with just a simple configuration! ⚡️
    </b>
</p>
<br />

<p align="center">
  <a href="https://github.com/getdozer/dozer/actions/workflows/dozer.yaml" target="_blank"><img src="https://github.com/getdozer/dozer/actions/workflows/dozer.yaml/badge.svg" alt="CI"></a>
  <a href="https://coveralls.io/github/getdozer/dozer?branch=main" target="_blank"><img src="https://coveralls.io/repos/github/getdozer/dozer/badge.svg?branch=main&t=kZMYaV&style=flat" alt="Coverage Status"></a>
  <a href="https://getdozer.io/docs/dozer" target="_blank"><img src="https://img.shields.io/badge/doc-reference-green" alt="Docs"></a>
  <a href="https://discord.com/invite/3eWXBgJaEQ" target="_blank"><img src="https://img.shields.io/badge/join-on%20discord-primary" alt="Join on Discord"></a>
  <a href="https://github.com/getdozer/dozer-python/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/badge/license-MIT-informational" alt="License"></a>

</p>
<br>

## Overview
This repository is a python wrapper over gRPC APIs that are automatically when you run [Dozer](https://github.com/getdozer/dozer).

## Installation

```bash
poetry add git+ssh://git@github.com:getdozer/dozer-python.git#main

# or 
pip install pydozer
```
## Dependencies

- [Dozer](https://github.com/getdozer/dozer)
- [Poetry](https://python-poetry.org/docs/)


### Querying

Intialize Users Endpoint
```python
api_client = ApiClient("users")

api_client.query()

# Query using $limit, $order_by, $filter
api_client.query({"$limit": 1})

#Count
api_client.count()
```


gRPC methods
```python
api_client.describe()

#Health
api_client.health()
```


### Ingestion

Initialize Ingestion Client
```
from dozer.ingest import IngestClient
ingestion_client = IngestClient()
```

Ingest a data frame

```python
df = pl.read_parquet('tests/trips_small.parquet')
ingestion_client.ingest_df('trips', df, seq_no=1)
```

Use [Arrow Format](https://github.com/apache/arrow) for ingestion
```python
ingestion_client.ingest_df_arrow('trips', df, seq_no=1)
```

Ingest raw records
```python
from pydozer.ingest_pb2 import IngestRequest
from pydozer.types_pb2 import Record, Value

user = IngestRequest(
    schema_name="users",
    typ=0,
    old=None,
    new=[Value(int_value=1), Value(string_value="vivek")],
    seq_no=1
)
ingestor.ingest(user)
```

Ingest in Arrow format

Check out our [Docs](https://getdozer.io/docs/dozer/) for more information.
### Testing
```
pytest
```

## Contributing

Please refer to [Contributing](https://getdozer.io/docs/contributing/overview) for more details.
