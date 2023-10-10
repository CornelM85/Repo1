from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep

class LeftMenu(BasePage):

    # selectors
    PROFILE_SECTION_BUTTON = '//span[text()="Profile"]'
    BOOK_STORE_SECTION_BUTTON = '//span[text()="Book Store"]'
    LOGIN_SECTION_BUTTON = '//span[text()="Login"]'

    # actions
    def click_profile_section(self):
        self.wait_for_elem(self.PROFILE_SECTION_BUTTON)
        element = self.driver.find_element(By.XPATH, self.PROFILE_SECTION_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def click_book_store_section(self):
        self.wait_for_elem(self.BOOK_STORE_SECTION_BUTTON)
        self.driver.find_element(By.XPATH, self.BOOK_STORE_SECTION_BUTTON).click()

    def login_section(self):
        self.wait_for_elem(self.LOGIN_SECTION_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_SECTION_BUTTON).click()

