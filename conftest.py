import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = 'function')
def browser():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
