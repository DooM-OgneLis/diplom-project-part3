from data import API
import requests
import allure


def delete_user(accessToken):
    requests.post(
                API.DELETE_USER,
                headers= {"Authorization": accessToken}
            )

@allure.step('Отправка формы POST на регистрацию нового пользователя')
def post_registration_user(email, password, name):
    register_form = {}
    register_form["email"] = email
    register_form["password"] = password
    register_form["name"] = name

    request = requests.post(
                        API.CREATE_USER,
                        json=register_form
                    )
    return request