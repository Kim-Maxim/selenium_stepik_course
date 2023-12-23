import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.set_capability("browserVersion", "118")
    chrome_options.add_argument("--log-level=1")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()
