# Задание: поиск элемента по тексту в ссылке

import math
import pytest
import allure

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage

@allure.feature('Задание 1-6-5')
class TestSearhOfElementByLink:
    @pytest.mark.smoke
    @allure.title('поиск элемента по тексту в ссылке')
    def test_search_of_element_by_link(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/find_link_text.html")
            main_page.open()
            person_info = next(generated_person())
            main_page.find_element_and_click((By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))))
            main_page.find_element_and_send_keys((By.NAME, "first_name"), person_info.firstname)
            main_page.find_element_and_send_keys((By.NAME, "last_name"), person_info.lastname)
            main_page.find_element_and_send_keys((By.NAME, "firstname"), person_info.city)
            main_page.find_element_and_send_keys((By.ID, "country"), person_info.country)
            main_page.find_element_and_click((By.CSS_SELECTOR, "button.btn"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"