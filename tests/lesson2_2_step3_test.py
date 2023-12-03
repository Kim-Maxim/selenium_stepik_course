# Задание: работа с выпадающим списком

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

@allure.suite('Задание 2-2-3')
class TestSelectList():
    @pytest.mark.smoke
    @allure.title('работа с выпадающим списком')
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
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task have failed"
