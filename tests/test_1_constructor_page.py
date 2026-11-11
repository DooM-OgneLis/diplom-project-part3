import pytest
import allure
from data import Urls, Pages
from pages.constructor_page import ConstructorPage
from locators.constructor_locators import ConstructorLocators as CL

class TestConstructionPage:

    @allure.title("Проверка перехода на страницу списка заказов")
    @allure.description(f"Проверить что при нажатии на ссылку 'Лента заказов' произойдет переход на {Pages.ORDER_FEED}")
    def test_click_in_list_order(self, driver):
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        err = constructor.click_on_order_feed_button()

        assert constructor.is_url_opened(Pages.ORDER_FEED), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        #дописать проверку загрузки заголовка страницы

    @allure.title("Проверка перехода на страницу конструктора")
    @allure.description(f"Проверить что при нажатии на ссылку 'Конструктор' произойдет переход на {Urls.STELLARBURGERS}")
    def test_click_in_constructor(self, driver):
        constructor = ConstructorPage(driver)
        constructor.url_start(Pages.ORDER_FEED)
        constructor.is_url_opened(Pages.ORDER_FEED) #дождаться загрузки страницы

        err = constructor.click_on_order_constructor_button()

        assert constructor.is_url_opened(Urls.STELLARBURGERS), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        #дописать проверку загрузки заголовка страницы

    @pytest.mark.parametrize(
            'ingredient, name_ingr',
            [[CL.BUN_CRATOR_N_200I, 'Краторная булка N-200i'], [CL.SAUS_FIRM_SPACE_SAUSE, 'Соус фирменный Space Sauce'], [CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA, 'Биокотлета из марсианской Магнолии']],
            ids = ['bun','sause','filling']
    )    
    def test_open_description_ingredient_in_click_on(self, driver, ingredient, name_ingr):
        allure.dynamic.title(f"Проверка открытия описания ингредиента '{name_ingr}'")
        allure.dynamic.description(f"Проверить что при нажатии на ингредиент '{name_ingr}', откроется окно с подробным описанием ингредиента")
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.click_element_with_wait(ingredient)
        
        assert constructor.find_element_with_wait(CL.SECTION_DETAL_INGR) #проверка появления окна с описанием ингредиента
        assert constructor.get_text_to_elements(CL.SECTION_DETAL_INGR_NAME) == name_ingr

    @allure.title("Проверка закрытия окна описания ингредиента нажатием на крестик")
    @allure.description(f"Проверить что при нажатии на крестик произойдет закрытие окна описания ингредиента")
    def test_closed_description_ingredient_in_click_cross(self, driver):
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.click_element_with_wait(CL.BUN_CRATOR_N_200I)
        constructor.find_element_with_wait(CL.SECTION_DETAL_INGR)

        constructor.click_element_with_wait(CL.BUTTON_CLOSE_SECTION_DETALI)

        assert constructor.check_close_windows_ingredient_info

    @pytest.mark.parametrize(
                'ingredient, ingredient_count, count',
                [[CL.BUN_CRATOR_N_200I, CL.BUN_CRATOR_N_200I_COUNT, '2'], [CL.SAUS_FIRM_SPACE_SAUSE, CL.SAUS_FIRM_SPACE_SAUSE_COUNT, '1'], [CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA, CL.FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA_COUNT, '1']],
                ids = ['bun','sause','filling']
        )  
    def test_add_ingredient(self, driver, ingredient, ingredient_count, count):
        allure.dynamic.title(f"Проверка добавления ингредиента '{ingredient}'")
        allure.dynamic.description(f"Проверить что при перетягивании '{ingredient}', он добавляется в рецепт бургера")
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы
        
        constructor.add_ingredient_to_burger(ingredient)

        assert constructor.get_text_to_elements(ingredient_count) == count
        