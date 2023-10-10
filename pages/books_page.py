from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys

class BooksPage(BasePage):
    # selectors
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_OF_BOOKS = '//div[@class= "action-buttons"]'
    SEARCH_INPUT = '//input[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'
    ADD_TO_YOUR_COLLECTION_BUTTON = '(//button[@id="addNewRecordButton"])[2]'
    BACK_TO_BOOK_STORE_BUTTON = '(//button[@id="addNewRecordButton"])[1]'

    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def fill_search_input(self, query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)

    def clear_search_input(self):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.send_keys(Keys.CONTROL, 'a')
        search.send_keys(Keys.BACKSPACE)

    def click_book_by_title(self, title):
        sleep(1)
        element = self.driver.find_element(By.XPATH, f'//a[text()="{title}"]')
        self.driver.execute_script("arguments[0].click();", element)
        #ori self.driver.find_element(By.XPATH, '//a[text()="' + title + '"]').click()

    def click_add_to_your_collection_button(self):
        self.wait_for_elem(self.ADD_TO_YOUR_COLLECTION_BUTTON)
        element = self.driver.find_element(By.XPATH, self.ADD_TO_YOUR_COLLECTION_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def click_back_to_book_store_button(self):
        self.wait_for_elem(self.BACK_TO_BOOK_STORE_BUTTON)
        element = self.driver.find_element(By.XPATH, self.BACK_TO_BOOK_STORE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    # validations
    def validate_correct_url(self):
        expected = 'https://demoqa.com/books'
        sleep(1)
        actual = self.driver.current_url
        self.assertEquals(expected, actual, 'URL is incorrect!')

    def validate_books_count(self, expected_number):
        sleep(1)
        actual_number = len(self.driver.find_elements(By.XPATH, self.NUMBER_OF_BOOKS))
        self.assertEquals(expected_number, actual_number, 'The number of books is incorrect!')

    def validate_book_title(self, expected_title):
        self.wait_for_elem(self.BOOK_TITLE)
        actual_title = self.driver.find_element(By.XPATH, self.BOOK_TITLE).text
        self.assertEquals(expected_title, actual_title, 'The book title is incorrect!')

