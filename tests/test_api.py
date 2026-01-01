import requests

def test_get_user():
    response = requests.get("http://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200
    assert "username" in response.json()