# Задание: ждем нужный текст на странице

import pytest
import allure

from locators.locators import LocatorsLesson2_4_step8
from pages.base_page import BasePage

@allure.feature('Задание 2-4-8')
class TestWaitByText():
    @pytest.mark.regress
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('ждем нужный текст на странице')
    def test_wait_by_text(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/explicit_wait2.html")
            main_page.open()
            locators = LocatorsLesson2_4_step8
            main_page.wait_text(locators.PRICE, "$100")
            main_page.find_element_and_click(locators.BOOK)
            x = main_page.find_element_and_text(locators.VALUE_X)
            y = main_page.calc(x)
            main_page.find_element_and_send_keys(locators.INPUT, y)       
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
