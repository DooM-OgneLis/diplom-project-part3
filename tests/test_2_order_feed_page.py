import pytest
import allure
from data import Urls, Pages
from pages.constructor_page import ConstructorPage
from pages.order_page import OrderFeedPage

class TestOrderFeedPage:

    @pytest.mark.parametrize(
                'counter',
                ['all_time', 'this_time'],
                ids = ['all_time','this_time']
        )    
    def test_Completed_within_the_entire_period(self, driver, registration_user, counter):
        allure.dynamic.title(f"Проверка изменения счетчика '{counter}' при заказе ")
        allure.dynamic.description(f"Проверить что при заказе, счетчик '{counter}' изменился")
        constructor = ConstructorPage(driver)
        order_feed = OrderFeedPage(driver)
        constructor.url_start(Pages.ORDER_FEED)
        constructor.is_url_opened(Pages.ORDER_FEED)

        this_count = order_feed.get_count_complite(counter)

        constructor.click_on_order_constructor_button()
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.add_ingredient_to_burger('bun')
        constructor.add_ingredient_to_burger('sause')      
        constructor.add_ingredient_to_burger('filling')
        constructor.click_button_order_create()
        constructor.url_start(Pages.ORDER_FEED)

        assert int(order_feed.get_count_complite(counter)) > int(this_count)

    @allure.title("Проверка добавление заказа в список 'В работе'")
    @allure.description(f"Проверить что при оформлении заказа, его номер появляется в списке 'В работе' на странице заказов")
    def test_add_order_in_order_worker_board(self, driver, registration_user):
        constructor = ConstructorPage(driver)
        order_feed = OrderFeedPage(driver)
        constructor.url_start(Urls.STELLARBURGERS) #для авторизации
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.add_ingredient_to_burger('bun')
        constructor.add_ingredient_to_burger('sause')      
        constructor.add_ingredient_to_burger('filling')
        constructor.click_button_order_create()
        this_order = constructor.get_number_of_order()
        constructor.url_start(Pages.ORDER_FEED)

        assert order_feed.check_number_order_in_list_order(this_order)

