import pytest

from product.services import get_service_data


@pytest.fixture
def mock_fetch_data(monkeypatch):
    def mock_fetch(url, method='GET', params=None, json=None):
        return {"key": "value"}

    monkeypatch.setattr('product.services.fetch_data', mock_fetch)


def test_get_service_data(mock_fetch_data):
    result = get_service_data()

    assert result == {"key": "value"}
