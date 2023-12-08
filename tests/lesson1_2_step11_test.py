# Запуск браузера и первый скрипт

import pytest
import allure

from locators.locators import LocatorsLesson1_2_step11
from pages.base_page import BasePage

@allure.feature('Задание 1-2-11')
class TestFirstScript:
    @pytest.mark.smoke
    @allure.title('запуск браузера и первый скрипт')
    def test_first_script(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/text_input_task.html")
            locators = LocatorsLesson1_2_step11
            main_page.open()
            main_page.find_element_and_send_keys(locators.INPUT, "get()")
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            assert alert_text == "Thank you for submitting the form!", "The task has failed"
