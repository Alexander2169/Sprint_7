import requests
import pytest
import allure
from config import BASE_URL


class СreatingОrder:
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

    def dictionary(self):
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

@pytest.mark.parametrize("creatingorder", [
    СreatingОrder("Кирилл", "Петров", "Москва", "Красные ворота",
           "85555555555", 5, "2024-09-29", "Всё хорошо!",
           ["BLACK"]),
    СreatingОrder("Дмитрий", "Союзов", "Москва", "Комсомольская",
           "88888888888", 7, "2024-09-30",
           "Всё хорошо!", ["GREY"]),
    СreatingОrder("Петр", "Петров", "Москва", "Южная",
           "89995001023", 9, "2024-10-01", "Всё хорошо!",
           ["BLACK", "GREY"]),
    СreatingОrder("Иван", "Иванов", "Москва", "Новокосино",
           "89995001025", 11, "2023-04-11", "Всё хорошо!", [])
])
@allure.title("Проверка создания заказа")
@allure.description("Проверка создания заказа с различными данными")
def test_create_order(creatingorder):
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=creatingorder.dictionary())

    assert response.status_code == 201
    response_json = response.json()
    assert "track" in response_json









