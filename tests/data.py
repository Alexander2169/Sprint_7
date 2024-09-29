test_data = {
    "valid_courier": {
        "login": "Sachaa",
        "password": "2169",
        "first_name": "dadic"
    },
    "empty_login": {
        "password": "5678",
        "first_name": "qwerty"
    },
    "empty_password": {
        "login": "Fantomas",
        "first_name": "qwerty"
    },
    "empty_both": {
        "first_name": "no_login_or_password"
    }
}

LOGIN_REQUIRED_MESSAGE = "Недостаточно данных для входа"
ACCOUNT_NOT_FOUND_MESSAGE = "Учетная запись не найдена"
INSUFFICIENT_DATA_MESSAGE = "Недостаточно данных для создания учетной записи"
