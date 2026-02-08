import requests


def test_get_users_list():
    url = "https://dummyjson.com/users"

    response = requests.get(url)

    # Status code
    assert response.status_code == 200

    data = response.json()

    # Verificăm structura răspunsului
    assert "users" in data
    assert len(data["users"]) > 0

def test_create_user():
    url = "https://dummyjson.com/users/add"

    payload = {
        "firstName": "Andrei",
        "lastName": "Axin",
        "age": 24
    }

    response = requests.post(url, json=payload)

    # Status code
    assert response.status_code == 201

    data = response.json()

    # Verificăm că datele trimise apar în răspuns
    assert data["firstName"] == "Andrei"
    assert data["lastName"] == "Axin"
    assert data["age"] == 24
    assert "id" in data

def test_update_user():
    user_id = 1
    url = f"https://dummyjson.com/users/{user_id}"

    payload = {
        "firstName": "UpdatedName",
        "age": 30
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["firstName"] == "UpdatedName"
    assert data["age"] == 30


def test_delete_user():
    user_id = 1
    url = f"https://dummyjson.com/users/{user_id}"

    response = requests.delete(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id
    assert data["isDeleted"] is True



