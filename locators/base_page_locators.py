from selenium.webdriver.common.by import By 

class BasePageLocators:
    BUTTON_CONSTRUCTOR_PAGE = (By.LINK_TEXT, "Конструктор")
    BUTTON_ORDER_FEED_PAGE = (By.LINK_TEXT, "Лента Заказов")
    FIRST_H_TAG = (By.XPATH, "//h1")