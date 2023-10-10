from pages.profile_page import ProfilePage
from behave import *

profile_page = ProfilePage()


@when('profile: I click on delete all books button')
def step_impl(context):
    profile_page.delete_all_books_button()
    profile_page.delete_book_alert_button()


@when('profile: I want to delete the book with title "{title}"')
def step_impl(context,title):
    profile_page.click_delete_book_by_title(title)
    profile_page.confirm_delete_book_alert_button()
    profile_page.alert_ok()

@then('profile: I want to check if the book with title "{title}" is present in the list')
def step_impl(context,title):
    profile_page.check_book_presence(title)


@then('profile: I want to check if the book with title "{title}" is not present in the list')
def step_impl(context,title):
    profile_page.check_book_removal(title)