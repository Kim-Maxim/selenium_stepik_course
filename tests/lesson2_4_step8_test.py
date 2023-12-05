# Задание: ждем нужный текст на странице

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.feature('Задание 2-4-8')
class TestWaitByText():
    @pytest.mark.smoke
    @allure.title('ждем нужный текст на странице')
    def test_wait_by_text(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/explicit_wait2.html")
            main_page.open()
            main_page.wait_text((By.XPATH, "//*[@id='price']"), "$100")
            main_page.find_element_and_click((By.XPATH, "//*[@id='book']"))
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='input_value']"))
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)       
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
