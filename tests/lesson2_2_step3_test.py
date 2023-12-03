# Задание: работа с выпадающим списком

import time
import pytest

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class TestSelectList():
    @pytest.mark.smoke
    def test_select_list(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/selects1.html")
            main_page.open()
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='num1']"))
            y = main_page.find_element_and_text((By.XPATH, "//*[@id='num2']"))
            sum = int(x) + int(y)
            select = Select(browser.find_element(By.TAG_NAME, "select"))
            select.select_by_value(str(sum))
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            time.sleep(0.5)
