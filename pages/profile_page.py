from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ProfilePage(BasePage):

    # selectors
    DELETE_ALL_BOOKS_BUTTON = '//button[text()="Delete All Books"]'
    CONFIRM_DELETE_BOOK_ALERT_BUTTON = '//button[@id="closeSmallModal-ok"]'

    # actions
    def delete_all_books_button(self):
        self.wait_for_elem(self.DELETE_ALL_BOOKS_BUTTON)
        element = self.driver.find_element(By.XPATH, self.DELETE_ALL_BOOKS_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def confirm_delete_book_alert_button(self):
        sleep(1)
        self.wait_for_elem(self.CONFIRM_DELETE_BOOK_ALERT_BUTTON)
        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_BOOK_ALERT_BUTTON).click()

    def click_delete_book_by_title(self, title):
        sleep(1)
        element = self.driver.find_element(By.XPATH, f'//a[text()="{title}"]/parent::span/parent::div/parent::div/parent::div//span[@id="delete-record-undefined"]')
        self.driver.execute_script("arguments[0].click();", element)

    # validations

    def check_book_presence(self, title):
        book = self.driver.find_elements(By.XPATH, f'//a[text()="{title}"]')
        self.assertEquals(1, len(book), 'Book is not found!')

    def check_book_removal(self, title):
        book = self.driver.find_elements(By.XPATH, f'//a[text()="{title}"]')
        self.assertEquals(0, len(book), 'Book is found!')