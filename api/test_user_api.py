import requests


def test_get_user_by_id():
    """
    API Test:
    Verify that a user can be retrieved by ID.

    Endpoint:
    GET /users/1

    Validations:
    - Status code is 200
    - Response contains correct user ID
    - Response contains username and email fields
    """

    # API endpoint
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Send GET request
    response = requests.get(url)

    # Validate HTTP status code
    assert response.status_code == 200

    # Parse JSON response
    response_body = response.json()

    # Validate response content
    assert response_body["id"] == 1
    assert "username" in response_body
    assert "email" in response_body




def test_get_non_existing_user():
    """
    Negative API Test:
    Verify that requesting a non-existing user returns 404
    """

    url = "https://jsonplaceholder.typicode.com/users/9999"

    response = requests.get(url)

    assert response.status_code == 404




def test_user_response_schema():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    body = response.json()

    # Schema validation (manual, lightweight)
    assert isinstance(body["id"], int)
    assert isinstance(body["name"], str)
    assert isinstance(body["username"], str)
    assert isinstance(body["email"], str)
    assert "@" in body["email"]



def test_get_user_response_time():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    # response.elapsed.total_seconds() returns response time
    assert response.elapsed.total_seconds() < 20