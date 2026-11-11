from selenium.webdriver.common.by import By 

class OrderFeedLocators:

    COMPLETED_ENTIRE_TIME_PERIOD = (By.XPATH, "//p[text() = 'Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    COMPLETED_ENTIRE_TODAY = (By.XPATH, "//p[text() = 'Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_IN_WORKING = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(normalize-space(.), '{}')]")