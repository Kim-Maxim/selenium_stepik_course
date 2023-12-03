# Задание: поиск сокровища с помощью get_attribute

import time
import pytest

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestGetAttribute():
    @pytest.mark.smoke
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
            time.sleep(0.5)
