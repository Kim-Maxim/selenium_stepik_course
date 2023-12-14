# Задание: поиск элементов с помощью Selenium

import pytest
import allure

from generator.generator import generated_person
from locators.locators import LocatorsLesson1_6_step4
from pages.base_page import BasePage

@allure.suite('Задание 1-6-4')
class TestSearhOfElements:

    @pytest.mark.regress
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.feature('поиск элементов с помощью Selenium')
    def test_search_of_elements(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/simple_form_find_task.html")
            main_page.open()
            locators = LocatorsLesson1_6_step4
            person_info = next(generated_person())
            main_page.find_element_and_send_keys(locators.FIRST_NAME, person_info.firstname)
            main_page.find_element_and_send_keys(locators.LAST_NAME, person_info.lastname)
            main_page.find_element_and_send_keys(locators.CITY, person_info.city)
            main_page.find_element_and_send_keys(locators.COUNTRY, person_info.country)
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"
            