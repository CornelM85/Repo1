from pages.logout_page import LogoutPage
from behave import *

logout_page = LogoutPage()


@when('logout: I click the logout button')
def step_impl(context):
    logout_page.click_logout_button()


@then('logout: I should land on login page')
def step_impl(context):
    logout_page.validate_correct_url()
