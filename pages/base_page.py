from data import Urls
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as BPL

class BasePage:
    @allure.step("инициализация базового драйвера браузера и установка времени ожидания")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.debug = []

    @allure.step("Открыть страницу в браузере")
    def url_start(self, url: str = Urls.STELLARBURGERS):
        self.driver.get(url)

    @allure.step("Ожидать, пока элемент станет видимым")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать, пока элемент исчезнет с экрана")
    def wait_close_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))


    """Ввиду возникающей проблемы автоматического нажатия в перегородки или мимо объектов,
    при исполнении сценария, добавлены 3 метода взаимодействия с объектами:
    base, java_script as js, action_chains as ac"""
    @allure.step("Кликнуть по элементу, дождавшись его кликабельности")
    def click_element_with_wait(self, locator, type_click = 'base'):        
        element = self.wait.until(EC.presence_of_element_located(locator)) #создание элемента по локатору

        if type_click == 'base':
            #обычный клик
            try:
                element.click()
                return 'Ok'
            except Exception as e:
                return f"ошибка: {e}"
        if type_click == 'js':
            #клик через скрипт
            self.driver.execute_script("arguments[0].click()", element)
            return 'Ok'
        if type_click == 'ac':
            #клик через действие
            AC(self.driver).move_to_element(element).click().perform()
            return 'Ok'
        return 'Error type click'

    @allure.step("Проскроллить к элементу в центр экрана")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

    @allure.step("перретянуть из А в Б")
    def drag_and_drop_to_element(self, dstart, dend):
        AC(self.driver).drag_and_drop(dstart, dend).perform()
    
    @allure.step("Вернуть текст элемента")
    def get_text_to_elements(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Проверить, что URL открыт")
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    @allure.step("открыть вкладку 'лента заказов'")
    def click_on_order_feed_button(self, type_click = 'base'):
        return self.click_element_with_wait(BPL.BUTTON_ORDER_FEED_PAGE, type_click)

    @allure.step("открыть вкладку 'Конструктор'")
    def click_on_order_constructor_button(self, type_click = 'base'):
        return self.click_element_with_wait(BPL.BUTTON_CONSTRUCTOR_PAGE, type_click)

    @allure.step("Найти заголовок страницы и вернуть текст")
    def search_h_tag_text(self):
        text = self.get_text_to_elements(BPL.FIRST_H_TAG)
        return text