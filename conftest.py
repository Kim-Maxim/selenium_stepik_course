import pytest
import allure

from selenium import webdriver
from datetime import datetime

@pytest.fixture(scope = 'function')
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    # attach = browser.get_screenshot_as_png()
    # allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    browser.quit()