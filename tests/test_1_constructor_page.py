import pytest
import allure
from data import Urls, Pages, Constant
from pages.constructor_page import ConstructorPage

class TestConstructionPage:

    @allure.title("Проверка перехода на страницу списка заказов")
    @allure.description(f"Проверить что при нажатии на ссылку 'Лента заказов' произойдет переход на {Pages.ORDER_FEED}")
    def test_click_in_list_order(self, driver):
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        err = constructor.click_on_order_feed_button()

        assert constructor.is_url_opened(Pages.ORDER_FEED), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        assert constructor.search_h_tag_text() == Constant.PAGE_H_TEXT['Заказы'], ('Страница имеет правильную ссылку, но название заголовка на странице неправильное, возможно загрузилась другая страница')

    @allure.title("Проверка перехода на страницу конструктора")
    @allure.description(f"Проверить что при нажатии на ссылку 'Конструктор' произойдет переход на {Urls.STELLARBURGERS}")
    def test_click_in_constructor(self, driver):
        constructor = ConstructorPage(driver)
        constructor.url_start(Pages.ORDER_FEED)
        constructor.is_url_opened(Pages.ORDER_FEED) #дождаться загрузки страницы

        err = constructor.click_on_order_constructor_button()

        assert constructor.is_url_opened(Urls.STELLARBURGERS), (f'клик вернул: {err}, переход на {Pages.ORDER_FEED} не произошел')
        assert constructor.search_h_tag_text() == Constant.PAGE_H_TEXT['Конструктор'], ('Страница имеет правильную ссылку, но название заголовка на странице неправильное, возможно загрузилась другая страница')

    @pytest.mark.parametrize(
            'ingredient, name_ingr',
            [['bun', 'Краторная булка N-200i'], ['sause', 'Соус фирменный Space Sauce'], ['filling', 'Биокотлета из марсианской Магнолии']],
            ids = ['bun','sause','filling']
    )    
    def test_open_description_ingredient_in_click_on(self, driver, ingredient, name_ingr):
        allure.dynamic.title(f"Проверка открытия описания ингредиента '{name_ingr}'")
        allure.dynamic.description(f"Проверить что при нажатии на ингредиент '{name_ingr}', откроется окно с подробным описанием ингредиента")
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.click_ingredient_type(ingredient)
        
        assert constructor.open_detal_ingredient() #проверка появления окна с описанием ингредиента
        assert constructor.get_detal_ingredient_name() == name_ingr

    @allure.title("Проверка закрытия окна описания ингредиента нажатием на крестик")
    @allure.description(f"Проверить что при нажатии на крестик произойдет закрытие окна описания ингредиента")
    def test_closed_description_ingredient_in_click_cross(self, driver):
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы

        constructor.click_ingredient_type()
        constructor.open_detal_ingredient()

        constructor.close_detal_ingredient()

        assert constructor.check_close_windows_ingredient_info

    @pytest.mark.parametrize(
                'ingredient, count',
                [['bun', '2'], ['sause', '1'], ['filling', '1']],
                ids = ['bun','sause','filling']
        )  
    def test_add_ingredient(self, driver, ingredient, count):
        allure.dynamic.title(f"Проверка добавления ингредиента '{ingredient}'")
        allure.dynamic.description(f"Проверить что при перетягивании '{ingredient}', он добавляется в рецепт бургера")
        constructor = ConstructorPage(driver)
        constructor.is_url_opened(Urls.STELLARBURGERS) #дождаться загрузки страницы
        
        constructor.add_ingredient_to_burger(ingredient)

        assert constructor.get_count_ingredients(ingredient) == count
        