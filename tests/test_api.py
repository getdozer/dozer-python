from tests.helper import api_client


def test_api_count(api_client):
    res = api_client.count()
    assert res is not None
    assert res.count is not None


def test_api_describe(api_client):
    res = api_client.describe()
    assert res is not None
    assert len(res) > 3


def test_api_health(api_client):
    res = api_client.health()
    assert res is not None
    # SERVING = 1
    assert res.status == 1


def test_api_query(api_client):
    res = api_client.query()
    assert res is not None
    assert res.records is not None
