import pytest
import allure
from data import Urls, Pages
from pages.constructor_page import ConstructorPage
from locators.constructor_locators import ConstructorLocators as CL
from locators.order_feed_locators import OrderFeedLocators as OFL
from selenium.webdriver.common.by import By 

class TestOrderFeedPage:

    @pytest.mark.parametrize(
                'counter',
                [OFL.COMPLETED_ENTIRE_TIME_PERIOD, OFL.COMPLETED_ENTIRE_TODAY],
                ids = ['all_time','this_time']
        )    
    def test_Completed_within_the_entire_period(self, driver, registration_user, counter):
        allure.dynamic.title(f"Проверка изменения счетчика '{counter}' при заказе ")
        allure.dynamic.description(f"Проверить что при заказе, счетчик '{counter}' изменился")
        constructor = ConstructorPage(driver)
        constructor.url_start(Pages.ORDER_FEED)
        constructor.is_url_opened(Pages.ORDER_FEED)

        this_count = constructor.get_text_to_elements(counter)

        constructor.click_on_order_constructor_button()
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.add_ingredient_to_burger(CL.BUN_CRATOR_N_200I)
        constructor.add_ingredient_to_burger(CL.SAUS_FIRM_SPACE_SAUSE)      
        constructor.add_ingredient_to_burger(CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA)
        constructor.click_element_with_wait(CL.BUTTON_ORDER_BOURGER)
        constructor.url_start(Pages.ORDER_FEED)

        assert int(constructor.get_text_to_elements(counter)) > int(this_count)

    @allure.title("Проверка добавление заказа в список 'В работе'")
    @allure.description(f"Проверить что при оформлении заказа, его номер появляется в списке 'В работе' на странице заказов")
    def test_add_order_in_order_worker_board(self, driver, registration_user):
        constructor = ConstructorPage(driver)
        constructor.url_start(Urls.STELLARBURGERS) #для авторизации
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.add_ingredient_to_burger(CL.BUN_CRATOR_N_200I)
        constructor.add_ingredient_to_burger(CL.SAUS_FIRM_SPACE_SAUSE)      
        constructor.add_ingredient_to_burger(CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA)
        constructor.click_element_with_wait(CL.BUTTON_ORDER_BOURGER)
        this_order = constructor.get_text_to_elements(CL.SECTION_DETAL_ORDER_NUMBER)
        constructor.url_start(Pages.ORDER_FEED)

        assert constructor.find_element_with_wait((By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(normalize-space(.), '{this_order}')]"))

