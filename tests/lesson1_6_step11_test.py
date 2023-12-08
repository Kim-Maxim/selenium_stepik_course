# Задание: уникальность селекторов

import pytest
import allure

from generator.generator import generated_person
from locators.locators import LocatorsLesson1_6_step11
from pages.base_page import BasePage

@allure.feature('Задание 1-6-11')
class TestUniqSelectors():
    @pytest.mark.smoke
    @allure.title('уникальность селекторов')
    def test_uniq_selectors(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/registration1.html")
            main_page.open()
            locators = LocatorsLesson1_6_step11
            person_info = next(generated_person())
            main_page.find_element_and_send_keys(locators.FIRST_NAME, person_info.firstname)
            main_page.find_element_and_send_keys(locators.LAST_NAME, person_info.lastname)
            main_page.find_element_and_send_keys(locators.EMAIL, person_info.email)
            main_page.find_element_and_send_keys(locators.PHONE, person_info.phone)
            main_page.find_element_and_send_keys(locators.ADDRESS, person_info.address)
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
            welcome_text = main_page.find_element_and_text(locators.TEXT)
        finally:
            assert welcome_text == "Congratulations! You have successfully registered!", "Welcome text is incorrect"
            