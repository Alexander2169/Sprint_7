import requests
from data import register_new_courier_and_return_login_password
from config import BASE_URL
import allure
class TestCreatingCourier:

    def setup_method(self):
        self.login_pass = register_new_courier_and_return_login_password()
        self.payload = {
            "login": self.login_pass[0],
            "password": self.login_pass[1],
            "firstName": self.login_pass[2]
        }

    def teardown_method(self):# Удаляем курьера после теста
        requests.delete(f"{BASE_URL}/api/v1/courier/{id}",
                    json={"login": self.payload["login"], "password": self.payload["password"]})

    @allure.title('Проверить, что курьера можно создать')
    def test_courier_can_be_created(self):
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=self.payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверить, что нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        requests.post(BASE_URL, json=self.payload)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=self.payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверить, что если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_with_missing_field(self):
        payload_missing_login = {
                "password": self.payload["password"],
                "firstName": self.payload["firstName"]
            }
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=payload_missing_login)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

        payload_missing_password = {
                "login": self.payload["login"],
                "firstName": self.payload["firstName"]
            }
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=payload_missing_password)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверить, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_courier_with_existing_login(self):
        requests.post(f"{BASE_URL}/api/v1/courier", json=self.payload)
        response = requests.post(f"{BASE_URL}/api/v1/courier", json=self.payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."















