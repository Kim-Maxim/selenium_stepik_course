# Задание на execute_script

import pytest

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestExcuteScript():
    @pytest.mark.smoke
    def test_execute_script(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/execute_script.html")
            main_page.open()
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='input_value']"))
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)
            main_page.find_element_and_click((By.XPATH, "//*[@id='robotCheckbox']"))
            main_page.go_to_element_and_click((By.XPATH, "//*[@id='robotsRule']"))
            main_page.go_to_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text)
