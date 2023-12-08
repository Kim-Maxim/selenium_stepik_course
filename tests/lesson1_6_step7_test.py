# Задание: использование метода find_elements

import pytest
import allure

from locators.locators import LocatorsLesson1_6_step7

@allure.suite('Задание 1-6-7')
class TestUseMethodByFindElements:
    @pytest.mark.smoke
    @allure.feature('использование метода find_elements')
    def test_use_method_by_find_elements(self, browser):
        locators = LocatorsLesson1_6_step7
        try:
            browser.get("http://suninjuly.github.io/huge_form.html")
            elements = browser.find_elements(*locators.INPUT)
            for element in elements:
                element.send_keys("Мой ответ")
            button = browser.find_element(*locators.BUTTON_SUBMIT)
            button.click()
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"
            