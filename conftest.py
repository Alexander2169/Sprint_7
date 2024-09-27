import pytest
import requests
from data import register_new_courier_and_return_login_password
from config import BASE_URL

@pytest.fixture()
def courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass

    requests.delete(f"{BASE_URL}/api/v1/courier/{id}", json={"login": login_pass[0], "password": login_pass[1]})
