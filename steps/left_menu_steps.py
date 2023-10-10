from pages.left_menu import LeftMenu
from behave import *

left_menu = LeftMenu()


@when('menu: I click profile section')
def step_impl(context):
    left_menu.click_profile_section()


@when('menu: I click on delete all books button')
def step_impl(context):
    left_menu.delete_all_books_button()
    left_menu.delete_all_books_alert_button()
