import requests
import pytest
from config import BASE_URL
import allure

class CreatingOrder:
    @pytest.mark.parametrize("color", [
        (None),  # Без цвета
        ("BLACK"),  # Один цвет
        ("GREY"),  # Другой цвет
        ("BLACK, GREY")  # Оба цвета
    ])
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в   шапке')
    def test_create_order(color):
        order_data = {
            "color": color
        }
        response = requests.post(BASE_URL, json=order_data)
        assert response.status_code == 201
        assert "track" in response.json()  # Проверяем, что возвращается track


