def test_home_route(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert response.json == {"data": "Welcome to API Home Page!"}


def test_about_route(client):
    response = client.get('/api/about')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "This is the About Page."
