import pytest
from django.urls import reverse
from django.test import Client
from product.models import Product


@pytest.fixture
def mock_get_service_data(monkeypatch):
    """Mock Get Service data."""
    mock_service_data = {'key': 'value'}
    monkeypatch.setattr(
        'product.views.get_service_data',
        lambda: mock_service_data
    )

    return mock_service_data


@pytest.mark.django_db
def test_product_list_view_with_client(mock_get_service_data):
    """Test product view."""
    Product.objects.create(title="Product 1", price=10.99)
    Product.objects.create(title="Product 2", price=20.99)

    client = Client()

    response = client.get(reverse('product-list'))

    assert response.status_code == 200

    data = response.json()

    assert 'products' in data
    assert 'external' in data

    assert len(data['products']) == 2

    assert data['products'][0]['title'] == "Product 1"
    assert data['products'][1]['title'] == "Product 2"

    assert data['external'] == {"key": "value"}
