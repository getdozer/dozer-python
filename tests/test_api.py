from tests.helper import dozer_server, api_client


def test_api_count(dozer_server, api_client):
    res = api_client.count()
    assert res is not None
    assert res.count is not None


def test_api_describe(dozer_server, api_client):
    res = api_client.describe()
    assert res is not None
    assert len(res) > 3


def test_api_health(dozer_server, api_client):
    res = api_client.health()
    assert res is not None
    # SERVING = 1
    assert res.status == 1


def test_api_query(dozer_server, api_client):
    res = api_client.query()
    assert res is not None
    assert res.records is not None
