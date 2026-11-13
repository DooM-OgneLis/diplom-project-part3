import pytest
import generator
import allure
from data import Urls
from selenium import webdriver

@pytest.fixture(scope="function", params=["chrome", "firefox"], ids=["chrome", "firefox"])
def driver(request):
    browser = request.param

    allure.dynamic.label("browser", browser)

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")
    
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
            allure.attach(
                body=f"Ошибка при удалении пользователя: {e!r}",
                name="Ошибка очистки (teardown)",
                attachment_type=allure.attachment_type.TEXT,
            )

