import requests

def test_create_user_missing_fields():
    url = "https://dummyjson.com/users/add"
    payload = {}

    response = requests.post(url, json=payload)

    assert response.status_code == 201 # Mock API does not validate input

def test_create_user_invalid_age():
    url = "https://dummyjson.com/users/add"

    payload = {
        "firstName": "Test",
        "lastName": "User",
        "age": "twenty"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201 # Mock API does not validate input

def test_get_non_existing_user():
    user_id = 999999
    url = f"https://dummyjson.com/users/{user_id}"

    response = requests.get(url)

    assert response.status_code == 404

def test_delete_user_twice():
    user_id = 1
    url = f"https://dummyjson.com/users/{user_id}"

    response1 = requests.delete(url)
    response2 = requests.delete(url)

    assert response1.status_code == 200
    assert response2.status_code == 200 # Mock API doesn't have real backend
