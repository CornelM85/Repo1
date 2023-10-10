Feature: Profile Capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click the login button
    When login: I login with user "Cornel" and password "Cornel12#$"

  @regression
  Scenario Outline: I add/remove books to my collection
    When books: I add to my collection the book with title "<book1>"
    When books: I add to my collection the book with title "<book2>"
    When menu: I click profile section
    Then profile: I want to check if the book with title "<book1>" is present in the list
    Then profile: I want to check if the book with title "<book2>" is present in the list
    When profile: I want to delete the book with title "<book1>"
    Then profile: I want to check if the book with title "<book1>" is not present in the list
    Then profile: I want to check if the book with title "<book2>" is present in the list
    When profile: I want to delete the book with title "<book2>"
    Then profile: I want to check if the book with title "<book2>" is not present in the list

    Examples:
    | book1            | book2               |
    | Git Pocket Guide | Speaking JavaScript |