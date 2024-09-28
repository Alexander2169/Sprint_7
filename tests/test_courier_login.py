import requests
import pytest
import allure

class Courier:
    def __init__(self, login: str, password: str, first_name: str = None):
        self.login = login
        self.password = password
        self.first_name = first_name


class CourierClient:
    BASE_URL = "http://qa-scooter.praktikum-services.ru"

    @staticmethod
    def get_post_request_courier_login(courier: Courier):
        return requests.post(f"{CourierClient.BASE_URL}/api/v1/courier/login", json={
            "login": courier.login,
            "password": courier.password
        })

@allure.feature("Courier Login Tests")
class TestCourierLogin:

    @allure.title("Курьер авторизирован")
    @allure.description("Проверка авторизации курьера с корректным логином и паролем")
    def test_check_creating_courier_login(self):
        courier_client = CourierClient()
        courier = Courier("Dadic", "21695", "qwerty")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 200
        assert "id" in response.json()
        print(response.status_code)

    @allure.title("Курьер авторизирован без логина")
    @allure.description("Проверка авторизации курьера без ввода логина")
    def test_check_verification_without_login_authorization(self):
        courier_client = CourierClient()
        courier = Courier("", "12345", "qwerty")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Курьер авторизирован без пароля")
    @allure.description("Проверка авторизации курьера без ввода пароля")
    def test_check_verification_without_password_authorization(self):
        courier_client = CourierClient()
        courier = Courier("Qwerty", "", "qwerty")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Курьер авторизирован под несуществующим логином")
    @allure.description("Проверка авторизации курьера в системе под несуществующим пользователем")
    def test_check_authorization_under_incorrect_login(self):
        courier_client = CourierClient()
        courier = Courier("QW", "159753")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Курьер авторизирован под некорректным логином")
    @allure.description("Проверка авторизации курьера в системе, если неправильно указать логин")
    def test_check_entering_invalid_login(self):
        courier_client = CourierClient()
        courier = Courier("Неделя", "159753")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Курьер авторизирован под некорректным паролем")
    @allure.description("Проверка авторизации курьера в системе, если неправильно указать пароль")
    def test_check_entering_invalid_password(self):
        courier_client = CourierClient()
        courier = Courier("Qwerty", "qwerty")
        response = courier_client.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
