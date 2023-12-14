# Задание: загрузка файла

import os
import pytest
import allure

from generator.generator import generated_person
from locators.locators import LocatorsLesson2_2_step8
from pages.base_page import BasePage

@allure.feature('Задание 2-2-8')
class TestUploadFile():
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('загрузка файла')
    def test_upload_file(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/file_input.html")
            main_page.open()
            locators = LocatorsLesson2_2_step8
            person_info = next(generated_person())
            main_page.find_element_and_send_keys(locators.FIRST_NAME, person_info.firstname)
            main_page.find_element_and_send_keys(locators.LAST_NAME, person_info.lastname)
            main_page.find_element_and_send_keys(locators.EMAIL, person_info.email)
            current_dir = os.path.abspath(os.path.dirname(__file__))    
            file_path = os.path.join(current_dir, 'text.txt')
            main_page.find_element_and_send_keys(locators.FILE, file_path)
            main_page.find_element_and_click(locators.BUTTON_SUBMIT)
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"
