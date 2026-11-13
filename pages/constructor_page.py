import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
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
    def add_ingredient_to_burger(self, ltype):
        '''Для текущего задания структура упрощена'''
        if ltype == 'bun':
            ingredient = self.find_element_with_wait(CL.BUN_CRATOR_N_200I)
        elif ltype == 'sause':
            ingredient = self.find_element_with_wait(CL.SAUS_FIRM_SPACE_SAUSE)
        elif ltype == 'filling':
            ingredient = self.find_element_with_wait(CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA)
        else:
            return "error: тип задан некоректно"
        
        burger = self.find_element_with_wait(CL.SECTION_LIST_BURGER)

        self.drag_and_drop_to_element(ingredient, burger)

    @allure.step("ожидать открытие окна")
    def open_detal_ingredient(self):
        try:
            self.find_element_with_wait(CL.SECTION_DETAL_INGR)
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текст имени ингредиента в карточке")
    def get_detal_ingredient_name(self):
        return self.get_text_to_elements(CL.SECTION_DETAL_INGR_NAME)

    @allure.step("Получить значение количества ингредиента")
    def get_count_ingredients(self, ltype = 'bun'):
        '''Для текущего задания структура упрощена'''
        if ltype == 'bun':
            return self.get_text_to_elements(CL.BUN_CRATOR_N_200I_COUNT)
        elif ltype == 'sause':
            return self.get_text_to_elements(CL.SAUS_FIRM_SPACE_SAUSE_COUNT)
        elif ltype == 'filling':
            return self.get_text_to_elements(CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA_COUNT) 
        else:
            return "error: тип задан некоректно"

    @allure.step("закрыть окно карточки ингредиента")
    def close_detal_ingredient(self):
        self.click_element_with_wait(CL.BUTTON_CLOSE_SECTION_DETALI)

    @allure.step("нажать на ингредиент")
    def click_ingredient_type(self, ltype = 'bun'):
        '''Для текущего задания структура упрощена'''
        if ltype == 'bun':
            self.click_element_with_wait(CL.BUN_CRATOR_N_200I)
        elif ltype == 'sause':
            self.click_element_with_wait(CL.SAUS_FIRM_SPACE_SAUSE)
        elif ltype == 'filling':
            self.click_element_with_wait(CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA) 
        else:
            return "error: тип задан некоректно"

    @allure.step("нажать на кнопку 'Оформить заказ'")
    def click_button_order_create(self):
        self.click_element_with_wait(CL.BUTTON_ORDER_BOURGER)

    @allure.step("Получить номер созданного заказа")
    def get_number_of_order(self):
        return self.get_text_to_elements(CL.SECTION_DETAL_ORDER_NUMBER)