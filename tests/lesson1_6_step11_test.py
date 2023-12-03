# Задание: уникальность селекторов

import time
import pytest

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage

class TestUniqSelectors():
    @pytest.mark.smoke
    def test_uniq_selectors(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/registration1.html")
            main_page.open()
            person_info = next(generated_person())
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Input your first name']"), person_info.firstname)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Input your last name']"), person_info.lastname)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Input your email']"), person_info.email)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Input your phone:']"), person_info.phone)
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, "input[placeholder='Input your address:']"), person_info.address)
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
            welcome_text = main_page.find_element_and_text((By.TAG_NAME, "h1"))
            assert welcome_text == "Congratulations! You have successfully registered!", "Welcome text is incorrect"
        finally:
            time.sleep(0.5)
