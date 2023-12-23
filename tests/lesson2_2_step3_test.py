# Задание: работа с выпадающим списком

import pytest
import allure

from locators.locators import LocatorsLesson2_2_step3
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


@allure.feature("Задание 2-2-3")
class TestSelectList:
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("работа с выпадающим списком")
    def test_select_list(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/selects1.html")
            main_page.open()
            locators = LocatorsLesson2_2_step3
            x = main_page.find_element_and_text(locators.NUM_1)
            y = main_page.find_element_and_text(locators.NUM_2)
            sum = int(x) + int(y)
            select = Select(browser.find_element(*locators.SELECT))
            select.select_by_value(str(sum))
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(":")[1])
            assert (
                "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:"
                in alert_text
            ), "The task has failed"
