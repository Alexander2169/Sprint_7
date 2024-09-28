from config import BASE_URL
import pytest
import requests
import allure

class CreatingOrder:
    @pytest.mark.parametrize([
        ("black", ["BLACK"]),
        ("grey", ["GREY"]),
        ("both_colors", ["BLACK", "GREY"]),
        ("no_color", [])
    ])
    def test_create_order(self, color):
        payload = {
            "firstName": "Александр",
            "lastName": "Тихомиров",
            "address": "Москва, Южная",
            "metroStation": 10,
            "phone": "+7 555 555 55 55",
            "rentTime": "3",
            "deliveryDate": "2024-09-30",
            "comment": "Спасибо, ждем",
            "color": color
        }
        response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()  # Проверяем, что возвращается track





