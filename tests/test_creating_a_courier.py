import random
import allure
from api_actions import CourierCreating, ClientCreating
from helpers import generate_random_string

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
        login = "Aleksads"
        password = "2169"
        first_name = "dadic"

        # Создаем первого курьера
        response = ClientCreating.create_courier(CourierCreating(login, password, first_name))
        assert response.status_code == 201

        # Создаем второго курьера с тем же логином
        response = ClientCreating.create_courier(CourierCreating(login, "4567", "qwerty"))
        assert response.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." in response.json().get("message")

    @allure.title('Проверяем, что если поле "Логин" не заполнено - запрос возвращает ошибку')
    def test_login_field_is_not_filled(self):
        password = "5678"
        first_name = "qwerty"

        courier = CourierCreating("", password, first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверяем, что если поле "Пароль" не заполнено - запрос возвращает ошибку')
    def test_password_field_is_not_filled(self):
        login = "Fantomas"
        first_name = "qwerty"

        courier = CourierCreating(login, "", first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверяем, что если поле "Логин" и "Пароль" не заполнены - запрос возвращает ошибку')
    def test_login_and_password_field_is_not_filled(self):
        first_name = "no_login_or_password"

        courier = CourierCreating("", "", first_name)
        response = ClientCreating.create_courier(courier)
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"



