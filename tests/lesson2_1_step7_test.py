# Задание: поиск сокровища с помощью get_attribute

import pytest
import allure

from locators.locators import LocatorsLesson2_1_step7
from pages.base_page import BasePage


@allure.feature("Задание 2-1-7")
class TestGetAttribute:
    @pytest.mark.regress
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("поиск сокровища с помощью get_attribute")
    def test_get_attribute(self, browser):
        try:
            main_page = BasePage(
                browser, "http://suninjuly.github.io/get_attribute.html"
            )
            main_page.open()
            locators = LocatorsLesson2_1_step7
            x = main_page.find_element_and_get_attribute(locators.VALUE_X, "valuex")
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)
            main_page.find_element_and_click(locators.CHECKBOX)
            main_page.find_element_and_click(locators.RADIOBUTTON)
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(":")[1])
            assert (
                "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:"
                in alert_text
            ), "The task has failed"
