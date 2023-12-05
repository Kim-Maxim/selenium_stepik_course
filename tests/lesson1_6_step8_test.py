# Задание: поиск элемента по XPath

import pytest
import allure

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage

@allure.suite('Задание 1-6-8')
class TestSearhOfElementByXpath:
    @pytest.mark.smoke
    @allure.title('поиск элемента по XPath')
    def test_search_of_element_by_xpath(self, browser):
        try:
            main_page = BasePage(browser, "http://suninjuly.github.io/find_xpath_form.html")
            main_page.open()
            person_info = next(generated_person())
            main_page.find_element_and_send_keys((By.NAME, "first_name"), person_info.firstname)
            main_page.find_element_and_send_keys((By.NAME, "last_name"), person_info.lastname)
            main_page.find_element_and_send_keys((By.NAME, "firstname"), person_info.city)
            main_page.find_element_and_send_keys((By.ID, "country"), person_info.country)
            main_page.find_element_and_click((By.XPATH, "//*[@type='submit']"))
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task has failed"
