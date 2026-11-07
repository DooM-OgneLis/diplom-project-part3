import pytest
import allure
from data import Urls, Pages
#from pages.order_feed import 
from pages.constructor import Constructor

class TestBaseFunction:

    @allure.title("Проверка перехода на страницу списка заказов")
    @allure.description(f"Проверить что при нажатии на ссылку 'Лента заказов' произойдет переход на {Pages.ORDER_FEED}")
    def test_click_in_list_order(self, driver):
        constructor = Constructor(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        err = constructor.click_on_order_feed_button()

        assert constructor.is_url_opened(Pages.ORDER_FEED), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        #дописать проверку загрузки заголовка страницы

    @allure.title("Проверка перехода на страницу списка заказов")
    @allure.description(f"Проверить что при нажатии на ссылку 'Конструктор' произойдет переход на {Urls.STELLARBURGERS}")
    def test_click_in_constructor(self, driver):
        constructor = Constructor(driver)
        constructor.url_start(Pages.ORDER_FEED)
        constructor.is_url_opened(Pages.ORDER_FEED) #дождаться загрузки страницы

        err = constructor.click_on_order_constructor_button()

        assert constructor.is_url_opened(Urls.STELLARBURGERS), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        #дописать проверку загрузки заголовка страницы

    @allure.title("Проверка открытия описания ингредиента")
    @allure.description(f"Проверить что при нажатии на ингредиент, откроется окно с подробным описанием ингредиента")
    def test_open_description_ingredient_in_click_on(self, driver):
        constructor = Constructor(driver)

        