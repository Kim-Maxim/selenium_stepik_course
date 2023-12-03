# Запуск браузера и первый скрипт

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.suite('Задание 1-2-11')
class TestFirstScript:
    @pytest.mark.smoke
    @allure.title('запуск браузера и первый скрипт')
    def test_first_script(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/text_input_task.html")
            main_page.open()
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, ".textarea"), "get()")
            main_page.find_element_and_click((By.CSS_SELECTOR, ".submit-submission"))
        finally:
            alert_text = browser.switch_to.alert.text
            assert alert_text == "Thank you for submitting the form!", "The task have failed"
