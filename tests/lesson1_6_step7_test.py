# Задание: использование метода find_elements

import pytest
import allure

from selenium.webdriver.common.by import By

@allure.suite('Задание 1-6-7')
class TestUseMethodByFindElements:
    @pytest.mark.smoke
    @allure.title('использование метода find_elements')
    def test_use_method_by_find_elements(self, browser):
        try:
            browser.get("http://suninjuly.github.io/huge_form.html")
            elements = browser.find_elements(By.XPATH, "//input[@type = 'text']")
            for element in elements:
                element.send_keys("Мой ответ")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
        finally:
            alert_text = browser.switch_to.alert.text
            print(alert_text.split(':')[1])
            assert "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text, "The task have failed"