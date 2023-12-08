# Задание: принимаем alert

import pytest
import allure

from locators.locators import LocatorsLesson2_3_step4
from pages.base_page import BasePage

@allure.feature('Задание 2-3-4')
class TestSwitchToAlert():
    @pytest.mark.smoke
    @allure.title('принимаем alert')
    def test_switch_to_alert(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/alert_accept.html")
            main_page.open()
            locators = LocatorsLesson2_3_step4
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
            browser.switch_to.alert.accept()
            x = main_page.find_element_and_text(locators.VALUE_X)
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)       
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
