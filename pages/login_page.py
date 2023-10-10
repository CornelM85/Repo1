from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):


    # selectors
    LOGIN_BUTTON = '//button[@id="login"]'
    USER_INPUT = '//input[@id="userName"]'
    PASS_INPUT = '//input[@id="password"]'
    INVALID_CREDENTIALS_ERROR = '//p[@id="name"]'

    # actions
    def input_username(self, user):
        self.wait_for_elem(self.USER_INPUT)
        self.driver.find_element(By.XPATH, self.USER_INPUT).send_keys(user)

    def input_password(self, user_pass):
        self.wait_for_elem(self.PASS_INPUT)
        self.driver.find_element(By.XPATH, self.PASS_INPUT).send_keys(user_pass)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # validations
    def validate_invalid_credentials_error(self):
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Invalid username or password!'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEquals(expected, actual, 'Error message is incorrect!')