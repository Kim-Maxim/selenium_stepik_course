import math
import allure

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @allure.step('открыть браузер')
    def open(self):
        self.browser.get(self.url)
    
    @allure.step('найти элемент и ввести данные')
    def find_element_and_send_keys(self, locator, text):
        self.browser.find_element(*locator).send_keys(text)
    
    @allure.step('найти элемент и кликнуть')
    def find_element_and_click(self, locator):
        self.browser.find_element(*locator).click()

    @allure.step('найти элемент и получить текст')
    def find_element_and_text(self, locator):
        return self.browser.find_element(*locator).text
    
    @allure.step('найти элемент и получить аттрибут')
    def find_element_and_get_attribute(self, locator, attr):
        return self.browser.find_element(*locator).get_attribute(attr)

    @allure.step('посчитать математическую формулу')
    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    @allure.step('перейти к элементу и кликнуть')
    def go_to_element_and_click(self, locator):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*locator))
        self.browser.find_element(*locator).click()

    @allure.step('подождать конкретного текста')
    def wait_text(self, locator, text, timeout = 15):
        return wait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))