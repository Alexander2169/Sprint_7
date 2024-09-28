from config import BASE_URL
import allure
import requests

class TestGetOrders():

    @allure.title('Проверяем, что в тело ответа возвращается список заказов')
    def test_get_orders_list(self):
        response = requests.get(f"{BASE_URL}/api/v1/orders")
        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)


