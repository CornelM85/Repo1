from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()


@when('login: I login with user "{user}" and password "{pswd}"')
def step_impl(context, user, pswd):
    login_page.input_username(user)
    login_page.input_password(pswd)
    login_page.click_login_button()


@then('login: I validate that error message is displayed')
def step_impl(context):
    login_page.validate_invalid_credentials_error()
