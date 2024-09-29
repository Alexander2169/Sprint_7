import pytest
import allure
from api_actions import CreatingOrder


@pytest.mark.parametrize("creatingorder", [
    CreatingOrder("Кирилл", "Петров", "Москва", "Красные ворота",
                  "85555555555", 5, "2024-09-29", "Всё хорошо!",
                  ["BLACK"]),
    CreatingOrder("Дмитрий", "Союзов", "Москва", "Комсомольская",
                  "88888888888", 7, "2024-09-30",
                  "Всё хорошо!", ["GREY"]),
    CreatingOrder("Петр", "Петров", "Москва", "Южная",
                  "89995001023", 9, "2024-10-01", "Всё хорошо!",
                  ["BLACK", "GREY"]),
    CreatingOrder("Иван", "Иванов", "Москва", "Новокосино",
                  "89995001025", 11, "2023-04-11", "Всё хорошо!", [])
])
@allure.title("Проверка создания заказа")
@allure.description("Проверка создания заказа с различными данными")
def test_create_order(creatingorder):
    response = creatingorder.create_order()

    assert response.status_code == 201
    response_json = response.json()
    assert "track" in response_json










