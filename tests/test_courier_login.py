import requests
from data import register_new_courier_and_return_login_password
import allure
import pytest

BASE_URL = "https://qa-scooter.praktikum-services.ru"

class TestCourierLogin:
    def setup_method(self):

        self.login_pass = register_new_courier_and_return_login_password()
        self.payload = {
            "login": self.login_pass[0],
            "password": self.login_pass[1]
        }
    @allure.title('Проверяем, что курьер может авторизоваться, переданы все обязательные поля')
    def test_login_courier(self):

        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json=self.payload)
        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title('Проверяем, что если поле "Логин" не заполнено - запрос возвращает ошибку')
    def test_login_field_is_not_filled(self):
        payload_without_login = {
            "password": self.payload["password"]
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json=payload_without_login)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


    @allure.title('Проверяем, что если поле "Пароль" не заполнено - запрос возвращает ошибку')
    @pytest.mark.xfail(reason="неверный статус код = 504")
    def test_password_field_is_not_filled(self):
        payload_without_password = {
            "login": self.payload["login"]
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json=payload_without_password)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверяем, что система вернёт ошибку, если неправильно указать Логин')
    def test_incorrect_login(self):
        incorrect_payload = {
            "login": "incorrect",
            "password": "password"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json=incorrect_payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
        print(response, response.json())
    @allure.title('Проверяем, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_authorization_of_a_non_existent_user(self):
        invalid_payload = {
            "login": "invalid",
            "password": "invalid"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", json=invalid_payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"












    def teardown_method(self):
        requests.delete(f"{BASE_URL}/api/v1/courier",
                    json={"login": self.payload["login"], "password": self.payload["password"]})



