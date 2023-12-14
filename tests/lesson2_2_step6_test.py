# Задание на execute_script

import pytest
import allure

from locators.locators import LocatorsLesson2_2_step6
from pages.base_page import BasePage

@allure.feature('Задание 2-2-6')
class TestExcuteScript():
    @pytest.mark.regress
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('работа с execute_script')
    def test_execute_script(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/execute_script.html")
            main_page.open()
            locators = LocatorsLesson2_2_step6
            x = main_page.find_element_and_text(locators.VALUE_X)
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)
            main_page.find_element_and_click(locators.CHECKBOX)
            main_page.go_to_element_and_click(locators.RADIOBUTTON)
            main_page.go_to_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
