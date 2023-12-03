# Задание: переход на новую вкладку

import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.suite('Задание 2-3-6')
class TestSwitchToNewTab():
    @pytest.mark.smoke
    @allure.title('переход на новую вкладку')
    def test_switch_to_new_tab(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/redirect_accept.html")
            main_page.open()
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
            browser.switch_to.window(browser.window_handles[1])
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='input_value']"))
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)       
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text)
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task have failed"
