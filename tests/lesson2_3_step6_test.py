# Задание: переход на новую вкладку

import pytest
import allure

from locators.locators import LocatorsLesson2_3_step6
from pages.base_page import BasePage

@allure.feature('Задание 2-3-6')
class TestSwitchToNewTab():
    @pytest.mark.smoke
    @allure.title('переход на новую вкладку')
    def test_switch_to_new_tab(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/redirect_accept.html")
            main_page.open()
            locators = LocatorsLesson2_3_step6
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
            browser.switch_to.window(browser.window_handles[1])
            x = main_page.find_element_and_text(locators.VALUE_X)
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)       
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
