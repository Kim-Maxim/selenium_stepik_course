# Задание: загрузка файла

import os
import pytest
import allure

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage

@allure.suite('Задание 2-2-8')
class TestUploadFile():
    @pytest.mark.smoke
    @allure.title('загрузка файла')
    def test_upload_file(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/file_input.html")
            main_page.open()
            person_info = next(generated_person())
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Enter first name']"), person_info.firstname)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Enter last name']"), person_info.lastname)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Enter email']"), person_info.email)
            current_dir = os.path.abspath(os.path.dirname(__file__))    
            file_path = os.path.join(current_dir, 'text.txt')
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='file']"), file_path)
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"
