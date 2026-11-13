import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from locators.order_feed_locators import OrderFeedLocators as OFL

class OrderFeedPage(BasePage):
    @allure.step("Вернуть значение счетчика")
    def get_count_complite(self, ctype):
        if ctype == 'all_time':
            return self.get_text_to_elements(OFL.COMPLETED_ENTIRE_TIME_PERIOD)
        elif ctype == 'this_time':
            return self.get_text_to_elements(OFL.COMPLETED_ENTIRE_TODAY)
        else:
            return "error: тип задан некоректно"

    @allure.step("найти номер заказа в списке")
    def check_number_order_in_list_order(self, order_num):
        try:
            self.find_element_with_wait((OFL.ORDER_IN_WORKING[0], OFL.ORDER_IN_WORKING[1].format(order_num)))
            return True
        except TimeoutException:
            return False