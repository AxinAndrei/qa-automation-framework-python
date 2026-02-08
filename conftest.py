import pytest
import logging
import requests
from utils.driver_factory import create_driver
from utils.config import get_browser, is_headless, get_base_url


@pytest.fixture
def driver():
    browser = get_browser()
    headless = is_headless()

    driver = create_driver(browser=browser, headless=headless)
    driver.get(get_base_url())

    yield driver
    driver.quit()


logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

@pytest.fixture
def api_test_user():
    url = "https://dummyjson.com/users/add"

    payload = {
        "firstName": "TestUser",
        "lastName": "Automation",
        "age": 99
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201

    user_data = response.json()
    yield user_data

    # cleanup (delete user)
    user_id = user_data["id"]
    requests.delete(f"https://dummyjson.com/users/{user_id}")