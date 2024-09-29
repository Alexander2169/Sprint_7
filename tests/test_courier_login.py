import allure
from api_actions import Courier, CourierClient

@allure.feature("Courier Login Tests")
class TestCourierLogin:

    @allure.title("Курьер авторизирован")
    @allure.description("Проверка авторизации курьера с корректным логином и паролем")
    def test_check_creating_courier_login(self):
        courier = Courier("Izumyshka", "12345", "izum")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Курьер авторизирован без логина")
    @allure.description("Проверка авторизации курьера без ввода логина")
    def test_check_verification_without_login_authorization(self):
        courier = Courier("", "12345", "qwer")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Курьер авторизирован без пароля")
    @allure.description("Проверка авторизации курьера без ввода пароля")
    def test_check_verification_without_password_authorization(self):
        courier = Courier("Qwerty", "", "qwerty")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Курьер авторизирован под несуществующим логином")
    @allure.description("Проверка авторизации курьера в системе под несуществующим пользователем")
    def test_check_authorization_under_incorrect_login(self):
        courier = Courier("QW", "159753")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Курьер авторизирован под некорректным логином")
    @allure.description("Проверка авторизации курьера в системе, если неправильно указать логин")
    def test_check_entering_invalid_login(self):
        courier = Courier("Неделя", "159753")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Курьер авторизирован под некорректным паролем")
    @allure.description("Проверка авторизации курьера в системе, если неправильно указать пароль")
    def test_check_entering_invalid_password(self):
        courier = Courier("Qwerty", "qwerty")
        response = CourierClient.get_post_request_courier_login(courier)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

