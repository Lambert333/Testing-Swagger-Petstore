from utils.data_generator import (
    generate_valid_user_payload,
    generate_invalid_user_payload,
    generate_users_array,
    generate_invalid_users_array
)
from endpoints.user_endpoint import UserEndpoint


# создание нового пользователя
def test_add_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.add_user(payload, 200)
    user.get_user_by_username(payload["username"], 200)
    user.check_field_value("id", payload["id"])


# создание нового пользователя с пустым телом запроса
def test_add_user_with_minimal_ata(session, base_url):
    # Примечание: API возвращает 200 вместо 400
    user = UserEndpoint(session=session, base_url=base_url)
    payload = {}
    user.add_user(payload, 200)


# создание пользователя с невалидными данными
def test_add_user_with_invalid_data(session, base_url):
    # Примечание: API возвращает 500 вместо 400
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_invalid_user_payload()
    user.add_user(payload, 500)  # API возвращает 500 вместо 400


# получение информации о пользователе
def test_get_user_by_username(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.add_user(payload, 200)
    user.get_user_by_username(payload["username"], 200)
    user.check_field_value("username", payload["username"])


# получение информации о несуществующем пользователе
def test_get_nonexistent_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    user.get_user_by_username("nonexistent_user", 404)


# обновление данных пользователя
def test_update_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.add_user(payload, 200)
    new_payload = generate_valid_user_payload()
    user.update_user(payload["username"], new_payload, 200)
    user.get_user_by_username(new_payload["username"], 200)
    user.check_field_value("username", new_payload["username"])


# обновление данных несуществующего пользователя
def test_update_nonexistent_user(session, base_url):
    # Примечание: API возвращает 200 вместо 404
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.update_user("nonexistent_user", payload, 200)


# удаление пользователя
def test_delete_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.add_user(payload, 200)
    user.delete_user(payload["username"], 200)
    user.get_user_by_username(payload["username"], 404)


# удаление несуществующего пользователя
def test_delete_nonexistent_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    user.delete_user("nonexistent_user", 404)


# авторизация пользователя
def test_login_user(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_valid_user_payload()
    user.add_user(payload, 200)
    user.login_user(payload["username"], payload["password"], 200)


# авторизация с неверными данными
def test_login_user_with_invalid_credentials(session, base_url):
    # Примечание: API возвращает 200 при невалидных данных
    user = UserEndpoint(session=session, base_url=base_url)
    user.login_user("invalid_user", "invalid_password", 200)


# авторизация с пустыми данными
def test_login_user_with_empty_credentials(session, base_url):
    # Примечание: API возвращает 200 при пустых полях данных
    user = UserEndpoint(session=session, base_url=base_url)
    user.login_user("", "", 200)


# завершение сеанса пользователя
def test_logout_user(session, base_url):
    # Примечание: API возвращает 200 даже если пользователь не был авторизован
    user = UserEndpoint(session=session, base_url=base_url)
    user.logout_user(200)


# создание нескольких пользователей через массив
def test_add_users_with_array(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_users_array(3)
    user.add_users_with_array(payload, 200)
    user.check_response_content(expected_code=200, message_contains="ok")


# создание нескольких пользователей через массив с невалидными данными
def test_add_users_with_invalid_array(session, base_url):
    # Примечание: API возвращает 500 вместо 400
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_invalid_users_array(3)
    user.add_users_with_array(payload, 500)


# создание нескольких пользователей через список
def test_add_users_with_list(session, base_url):
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_users_array(3)
    user.add_users_with_list(payload, 200)
    user.check_response_content(expected_code=200, message_contains="ok")


# создание нескольких пользователей через список с невалидными данными
def test_add_users_with_invalid_list(session, base_url):
    # Примечание: API возвращает 500 вместо 400
    user = UserEndpoint(session=session, base_url=base_url)
    payload = generate_invalid_users_array(3)
    user.add_users_with_list(payload, 500)
