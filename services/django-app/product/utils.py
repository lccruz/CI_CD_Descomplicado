import requests


def fetch_data(url, method='GET', params=None, json=None):
    """
    Fetches JSON data from a given URL using HTTP methods.

    Args:
        url (str): The URL from which to fetch the data.
        method (str, optional): The HTTP method to use, defaults to 'GET'.
        params (dict, optional): Dictionary or bytes to be sent in the query string of the request.
        json (dict, optional): JSON data to send in the body of the request.

    Returns:
        dict or None: JSON response as a Python dictionary if successful, None if there's an error.
    """
    headers = {
        'Content-Type': 'application/json',
    }
    kwargs = dict(
        json=json,
        params=params,
        headers=headers,
        timeout=10
    )
    try:
        response = requests.request(method.upper(), url, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
