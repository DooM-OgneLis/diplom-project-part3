from selenium.webdriver.common.by import By 

class ConstructorLocators:
    BUN_CRATOR_N_200I = (By.XPATH, "//p[normalize-space()='Краторная булка N-200i']")
    SAUS_FIRM_SPACE_SAUSE = (By.XPATH, "//p[normalize-space()='Соус фирменный Space Sauce']")
    FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA = (By.XPATH, "//p[normalize-space()='Биокотлета из марсианской Магнолии']")

    BUN_CRATOR_N_200I_COUNT = (By.XPATH, 
                            "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')]"
                            "[.//p[normalize-space()='Краторная булка N-200i']]"
                            "//p[contains(@class, 'counter_counter__num')]")
    SAUS_FIRM_SPACE_SAUSE_COUNT = (By.XPATH, 
                            "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')]"
                            "[.//p[normalize-space()='Соус фирменный Space Sauce']]"
                            "//p[contains(@class, 'counter_counter__num')]")
    FILLING_BIOCOTLET_FROM_MARTIAN_MAGNOLIA_COUNT = (By.XPATH, 
                            "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')]"
                            "[.//p[normalize-space()='Биокотлета из марсианской Магнолии']]"
                            "//p[contains(@class, 'counter_counter__num')]")
    
    
    '''В виду абсолютной индетичности кнопок в разных секциях, в поискойвый 
    запрос добавлен фильтр секции для исключения вариантов объектов'''
    BUTTON_CLOSE_SECTION_DETALI = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]/*/button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    BUTTON_ORDER_BOURGER = (By.XPATH, "//Button[text() = 'Оформить заказ']")

    SECTION_DETAL_ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]"
                                  "//h2")
    SECTION_LIST_BURGER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    SECTION_DETAL_INGR = (By.XPATH, "//h2[text() = 'Детали ингредиента']/../../..") #найти текст секции и спустится до уровня секции, так гарантируется нахождение только 1 экземпляра
    SECTION_DETAL_INGR_NAME = (By.XPATH, "//h2[text() = 'Детали ингредиента']/../p") #спускаемся на 1 уровень и находим имя ингредиента
    
