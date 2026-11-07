from selenium.webdriver.common.by import By 

class ConstructorLocators:
    BUN_CRATOR_N_200I = (By.LINK_TEXT, "Краторная булка N-200i")
    SAUS_FIRM_SPACE_SAUSE = (By.LINK_TEXT, "Соус фирменный Space Sauce")
    
    '''В виду абсолютной индетичности кнопок в разных секциях, в поискойвый 
    запрос добавлен фильтр секции для исключения вариантов объектов'''
    BUTTON_CLOSE_SECTION_DETALI = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]/*/button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")

    SECTION_LIST_BURGER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
