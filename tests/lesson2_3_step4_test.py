# Задание: принимаем alert

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.feature('Задание 2-3-4')
class TestSwitchToAlert():
    @pytest.mark.smoke
    @allure.title('принимаем alert')
    def test_switch_to_alert(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/alert_accept.html")
            main_page.open()
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
            browser.switch_to.alert.accept()
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='input_value']"))
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)       
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
