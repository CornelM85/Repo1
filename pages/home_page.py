from selenium.webdriver.common.by import By
from base_page import BasePage


class HomePage(BasePage):
    # selectors
    BOOK_STORE_APPLICATION_CARD = '//h5[text() = "Book Store Application"]/parent::div/parent::div'

    # actions
    def navigate_to_home_page(self):
        self.driver.get('https://demoqa.com/')
        #self.driver.execute_script('document.body.style.zoom="50%"')
        #sleep(2)

    def click_book_store_application_card(self):
        self.wait_for_elem(self.BOOK_STORE_APPLICATION_CARD)
        self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD).click()
