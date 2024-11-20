from django.conf import settings

from product.utils import fetch_data


def get_service_data():
    """Get service data."""
    url = settings.SERVICE_API_URL

    return fetch_data(url, 'GET')
