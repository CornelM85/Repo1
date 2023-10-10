from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LogoutPage(BasePage):
    # selectors
    LOGOUT_BUTTON = '//button[@id="submit"]'

    # actions
    def click_logout_button(self):
        self.wait_for_elem(self.LOGOUT_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGOUT_BUTTON).click()

    # validations
    def validate_correct_url(self):
        expected = 'https://demoqa.com/login'
        sleep(1)
        actual = self.driver.current_url
        self.assertEquals(expected, actual, 'URL is incorrect!')