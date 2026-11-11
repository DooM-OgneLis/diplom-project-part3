import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from locators.constructor_locators import ConstructorLocators as CL

class ConstructorPage(BasePage):
    @allure.step("Ожидать закрытие окна")
    def check_close_windows_ingredient_info(self):
        try:
            self.wait_close_element(CL.SECTION_LIST_BURGER)
            return True
        except TimeoutException:
            return False
        
    @allure.step("Добавить ингредиент в рецепт")
    def add_ingredient_to_burger(self, locator):
        ingredient = self.driver.find_element(*locator)
        burger = self.driver.find_element(*CL.SECTION_LIST_BURGER)

        ActionChains(self.driver).drag_and_drop(ingredient, burger).perform()