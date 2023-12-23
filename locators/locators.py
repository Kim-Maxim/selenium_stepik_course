from selenium.webdriver.common.by import By


class LocatorsLesson1_2_step11:
    INPUT = (By.CSS_SELECTOR, ".textarea")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".submit-submission")


class LocatorsLesson1_6_step4:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    CITY = (By.NAME, "firstname")
    COUNTRY = (By.ID, "country")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button.btn")


class LocatorsLesson1_6_step5:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    CITY = (By.NAME, "firstname")
    COUNTRY = (By.ID, "country")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button.btn")


class LocatorsLesson1_6_step7:
    INPUT = (By.XPATH, "//input[@type = 'text']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson1_6_step8:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    CITY = (By.NAME, "firstname")
    COUNTRY = (By.ID, "country")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson1_6_step11:
    FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder='Input your email']")
    PHONE = (By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")
    TEXT = (By.TAG_NAME, "h1")


class LocatorsLesson2_1_step5:
    VALUE_X = (By.XPATH, "//*[@id='input_value']")
    INPUT = (By.XPATH, "//*[@id='answer']")
    CHECKBOX = (By.XPATH, "//*[@id='robotCheckbox']")
    RADIOBUTTON = (By.XPATH, "//*[@id='robotsRule']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson2_1_step7:
    VALUE_X = (By.XPATH, "//*[@id='treasure']")
    INPUT = (By.XPATH, "//*[@id='answer']")
    CHECKBOX = (By.XPATH, "//*[@id='robotCheckbox']")
    RADIOBUTTON = (By.XPATH, "//*[@id='robotsRule']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson2_2_step3:
    NUM_1 = (By.XPATH, "//*[@id='num1']")
    NUM_2 = (By.XPATH, "//*[@id='num2']")
    SELECT = (By.TAG_NAME, "select")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson2_2_step6:
    VALUE_X = (By.XPATH, "//*[@id='input_value']")
    INPUT = (By.XPATH, "//*[@id='answer']")
    CHECKBOX = (By.XPATH, "//*[@id='robotCheckbox']")
    RADIOBUTTON = (By.XPATH, "//*[@id='robotsRule']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson2_2_step8:
    FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder='Enter email']")
    FILE = (By.XPATH, "//*[@id='file']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")


class LocatorsLesson2_3_step4:
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")
    VALUE_X = (By.XPATH, "//*[@id='input_value']")
    INPUT = (By.XPATH, "//*[@id='answer']")


class LocatorsLesson2_3_step6:
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")
    VALUE_X = (By.XPATH, "//*[@id='input_value']")
    INPUT = (By.XPATH, "//*[@id='answer']")


class LocatorsLesson2_4_step8:
    PRICE = (By.XPATH, "//*[@id='price']")
    BOOK = (By.XPATH, "//*[@id='book']")
    BUTTON_SUBMIT = (By.XPATH, "//*[@type='submit']")
    VALUE_X = (By.XPATH, "//*[@id='input_value']")
    INPUT = (By.XPATH, "//*[@id='answer']")
