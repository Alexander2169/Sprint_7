import requests
from config import BASE_URL

class Courier:
    def __init__(self, login: str, password: str, first_name: str = None):
        self.login = login
        self.password = password
        self.first_name = first_name

class Client:
    @staticmethod
    def get_post_request_courier_login(courier: Courier):
        return requests.post(f"{BASE_URL}/api/v1/courier/login", json={
            "login": courier.login,
            "password": courier.password
        })