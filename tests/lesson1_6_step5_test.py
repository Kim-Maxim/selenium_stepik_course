# Задание: поиск элемента по тексту в ссылке

import math
import time
import pytest

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage

class TestSearhOfElementByLink:
    @pytest.mark.smoke
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
            time.sleep(0.5)
