import requests
from config import BASE_URL

class CourierLogin:
    def __init__(self, login: str, password: str, first_name: str = None):
        self.login = login
        self.password = password
        self.first_name = first_name

class ClientLogin:
    @staticmethod
    def get_post_request_courier_login(courier: CourierLogin):
        return requests.post(f"{BASE_URL}/api/v1/courier/login", json={
            "login": courier.login,
            "password": courier.password
        })

class CourierCreating:
    def __init__(self, login: str, password: str, first_name: str = None):
        self.login = login
        self.password = password
        self.first_name = first_name

    def to_json(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }

class ClientCreating:

    @staticmethod
    def create_courier(courier: CourierCreating):
        return requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())