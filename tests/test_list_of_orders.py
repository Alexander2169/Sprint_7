import allure
import requests
from api_actions import *


class TestListOrders():

    @allure.title('Проверяем, что в тело ответа возвращается список заказов')
    def test_get_orders_list(self):
        response = requests.get(f"{BASE_URL}/api/v1/orders")
        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)


