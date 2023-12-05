# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

import pytest
import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@allure.feature('Задание 2-1-5')
class TestClickCheckboxAndRadiobutton():
    @pytest.mark.smoke
    @allure.title('кликаем по checkboxes и radiobuttons (капча для роботов)')
    def test_click_checkbox_and_radiobutton(self, browser):
        try:
            main_page = BasePage(browser, "https://suninjuly.github.io/math.html")
            main_page.open()
            x = main_page.find_element_and_text((By.XPATH, "//*[@id='input_value']"))
            y = main_page.calc(x)
            main_page.find_element_and_send_keys((By.XPATH, "//*[@id='answer']"), y)
            main_page.find_element_and_click((By.XPATH, "//*[@id='robotCheckbox']"))
            main_page.find_element_and_click((By.XPATH, "//*[@id='robotsRule']"))
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:" in alert_text, "The task has failed"
