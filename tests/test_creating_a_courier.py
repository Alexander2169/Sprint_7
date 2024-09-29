import requests
import random
import string
import allure
from config import BASE_URL

class Courier:
    def __init__(self, login, password, first_name=None):
        self.login = login
        self.password = password
        self.first_name = first_name

    def to_json(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


class TestCreatingCourier:
    @allure.title('Проверяем, что можно создать курьера')
    def test_create_courier(self):
        login = generate_random_string(random.randint(2, 15))
        password = generate_random_string(random.randint(7, 15))
        first_name = generate_random_string(random.randint(2, 18))

        courier = Courier(login, password, first_name)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title('Проверяем, что можно создать курьера без имени')
    def test_create_courier_without_first_name(self):
        login = generate_random_string(random.randint(2, 15))
        password = generate_random_string(random.randint(7, 15))

        courier = Courier(login, password)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        login = "Aleksadу"
        password = "2169"
        first_name = "dadic"

        # Создаем первого курьера
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=Courier(login, password, first_name).to_json())
        assert response.status_code == 201

        # Создаем второго курьера с тем же логином
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=Courier(login, "4567",
                                                                            "qwerty").to_json())
        assert response.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." in response.json().get("message")

    @allure.title('Проверяем, что если поле "Логин" не заполнено - запрос возвращает ошибку')
    def test_login_field_is_not_filled(self):
        password = "5678"
        first_name = "qwerty"

        courier = Courier("", password, first_name)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"


    @allure.title('Проверяем, что если поле "Пароль" не заполнено - запрос возвращает ошибку')
    def test_password_field_is_not_filled(self):
        login = "Fantomas"
        first_name = "qwerty"

        courier = Courier(login, "", first_name)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверяем, что если полля "Логин" и "Пароль" не заполнены - запрос возвращает ошибку')
    def test_login_and_password_field_is_not_filled(self):
        first_name = "no_login_or_password"

        courier = Courier("", "", first_name)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=courier.to_json())
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

