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