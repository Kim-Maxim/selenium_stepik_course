# Задание: поиск сокровища с помощью get_attribute

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.suite('Задание 2-1-7')
class TestGetAttribute():
    @pytest.mark.smoke
    @allure.title('поиск сокровища с помощью get_attribute')
    def test_get_attribute(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/get_attribute.html")
            main_page.open()
            x = main_page.find_element_and_get_attribute((By.XPATH, "//*[@id='treasure']"), "valuex")
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)
            main_page.find_element_and_click((By.XPATH, "//*[@id='robotCheckbox']"))
            main_page.find_element_and_click((By.XPATH, "//*[@id='robotsRule']"))
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text)
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task have failed"
