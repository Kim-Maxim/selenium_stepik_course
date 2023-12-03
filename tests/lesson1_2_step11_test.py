# Запуск браузера и первый скрипт

import time
import pytest

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestFirstScript:
    @pytest.mark.smoke
    def test_first_script(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/text_input_task.html")
            main_page.open()
            main_page.find_element_and_send_keys((By.CSS_SELECTOR, ".textarea"), "get()")
            main_page.find_element_and_click((By.CSS_SELECTOR, ".submit-submission"))
        finally:
            time.sleep(0.5)
