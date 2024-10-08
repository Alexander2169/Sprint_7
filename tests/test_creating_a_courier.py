import random
import allure
from api_actions import CourierCreating, ClientCreating
from helpers import generate_random_string
from data import *

class TestCreatingCourier:

    @allure.title('Проверяем, что можно создать курьера')
    def test_create_courier(self):
        login = generate_random_string(random.randint(2, 15))
        password = generate_random_string(random.randint(7, 15))
        first_name = generate_random_string(random.randint(2, 18))

        courier = CourierCreating(login, password, first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title('Проверяем, что можно создать курьера без имени')
    def test_create_courier_without_first_name(self):
        login = generate_random_string(random.randint(2, 15))
        password = generate_random_string(random.randint(7, 15))

        courier = CourierCreating(login, password)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        login = test_data["valid_courier"]["login"]
        password = test_data["valid_courier"]["password"]
        first_name = test_data["valid_courier"]["first_name"]

        # Создаем первого курьера
        response = ClientCreating.create_courier(CourierCreating(login, password, first_name))
        assert response.status_code == 201

        # Создаем второго курьера с тем же логином
        response = ClientCreating.create_courier(CourierCreating(login, "4567", "qwerty"))
        assert response.status_code == 409
        assert DUBLICATE_LOGIN in response.json().get("message")

    @allure.title('Проверяем, что если поле "Логин" не заполнено - запрос возвращает ошибку')
    def test_login_field_is_not_filled(self):
        password = test_data["empty_login"]["password"]
        first_name = test_data["empty_login"]["first_name"]

        courier = CourierCreating("", password, first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == MISSING_DATA

    @allure.title('Проверяем, что если поле "Пароль" не заполнено - запрос возвращает ошибку')
    def test_password_field_is_not_filled(self):
        login = test_data["empty_password"]["login"]
        first_name = test_data["empty_password"]["first_name"]

        courier = CourierCreating(login, "", first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == MISSING_DATA

    @allure.title('Проверяем, что если поле "Логин" и "Пароль" не заполнены - запрос возвращает ошибку')
    def test_login_and_password_field_is_not_filled(self):
        first_name = test_data["empty_both"]["first_name"]

        courier = CourierCreating("", "", first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == MISSING_DATA


