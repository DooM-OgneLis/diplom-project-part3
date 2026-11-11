import pytest
import generator
from data import Urls
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(Urls.STELLARBURGERS)
    yield driver
    driver.quit()

import API.user_api as UA

@pytest.fixture(scope="function")
def registration_user(driver):
    email = generator.email_generator()
    password = generator.password_generator()
    name = generator.name_generator()

    reqest = UA.post_registration_user(email, password, name)

    yield driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);"
        "window.localStorage.setItem('refreshToken', arguments[1]);",
        reqest.json()["accessToken"],
        reqest.json()["refreshToken"]
    )
    try:
        UA.delete_user(reqest.json()['accessToken'])
    except Exception as e:
        print(f"[Cleanup] Ошибка удаления: {e}")

