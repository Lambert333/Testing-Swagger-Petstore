from utils.base_endpoint import BaseEndpoint


class UserEndpoint(BaseEndpoint):

    # создаем нового пользователя с помощью метода POST
    def add_user(self, payload, expected_status):
        return self.post(f"/user", payload=payload, expected_status=expected_status)

    # получаем информацию о пользователе по username с помощью метода GET
    def get_user_by_username(self, username, expected_status):
        return self.get(f"/user/{username}", expected_status=expected_status)

    # обновляем данные пользователя с помощью метода PUT
    def update_user(self, username, payload, expected_status):
        return self.put(f"/user/{username}", payload=payload, expected_status=expected_status)

    # удаляем пользователя с помощью метода DELETE
    def delete_user(self, username, expected_status):
        return self.delete(f"/user/{username}", expected_status=expected_status)

    # авторизация пользователя с помощью метода GET
    def login_user(self, username, password, expected_status):
        return self.get(f"/user/login?username={username}&password={password}", expected_status=expected_status)

    # завершение сеанса пользователя (логаут) с помощью метода GET
    def logout_user(self, expected_status):
        return self.get(f"/user/logout", expected_status=expected_status)

    # создание нескольких пользователей через массив с помощью метода POST
    def add_users_with_array(self, payload, expected_status):
        return self.post(f"/user/createWithArray", payload=payload, expected_status=expected_status)

    # создание нескольких пользователей через список с помощью метода POST
    def add_users_with_list(self, payload, expected_status):
        return self.post(f"/user/createWithList", payload=payload, expected_status=expected_status)
