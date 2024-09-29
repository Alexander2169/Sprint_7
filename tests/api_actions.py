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

class CreatingOrder:
    def __init__(self, first_name, last_name, address, subway_station, phone, rent_time, delivery_date, comment, color):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.subway_station = subway_station
        self.phone = phone
        self.rent_time = rent_time
        self.delivery_date = delivery_date
        self.comment = comment
        self.color = color

    def to_dict(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "address": self.address,
            "station": self.subway_station,
            "phone": self.phone,
            "rentTime": self.rent_time,
            "deliveryDate": self.delivery_date,
            "comment": self.comment,
            "color": self.color
        }

    def create_order(self):
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=self.to_dict())
        return response