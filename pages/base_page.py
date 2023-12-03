import math


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_element_and_send_keys(self, locator, text):
        self.browser.find_element(*locator).send_keys(text)
    
    def find_element_and_click(self, locator):
        self.browser.find_element(*locator).click()

    def find_element_and_text(self, locator):
        return self.browser.find_element(*locator).text
    
    def find_element_and_get_attribute(self, locator, attr):
        return self.browser.find_element(*locator).get_attribute(attr)

    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    def go_to_element_and_click(self, locator):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.browser.find_element(*locator))
        self.browser.find_element(*locator).click()
