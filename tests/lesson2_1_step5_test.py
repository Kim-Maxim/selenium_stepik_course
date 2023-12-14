# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

import pytest
import allure

from locators.locators import LocatorsLesson2_1_step5
from pages.base_page import BasePage

@allure.feature('Задание 2-1-5')
class TestClickCheckboxAndRadiobutton():
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('кликаем по checkboxes и radiobuttons (капча для роботов)')
    def test_click_checkbox_and_radiobutton(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/math.html")
            main_page.open()
            locators = LocatorsLesson2_1_step5
            x = main_page.find_element_and_text(locators.VALUE_X)
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)
            main_page.find_element_and_click(locators.CHECKBOX)
            main_page.find_element_and_click(locators.RADIOBUTTON)
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
