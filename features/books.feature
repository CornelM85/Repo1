Feature: Books Capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click the login button
    When login: I login with user "Cornel" and password "Cornel12#$"

  @regression
  Scenario: I validate the stock count
    Then books: I validate that 8 are displayed

  @regression
  Scenario Outline: I validate that the search is working
    When books: I search after "<query>"
    Then books: I validate that only "Git Pocket Guide" book is displayed

  Examples:
    | query  |
    | GIT     |
    | Richard |

  @regression
  Scenario: I validate that clear search is working
    When books: I search after "test"
    When books: I clear search input
    Then books: I validate that 8 are displayed