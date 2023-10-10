Feature: Logout Capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click the login button
    When login: I login with user "Cornel" and password "Cornel12#$"

 @regression
  Scenario: I logged out
    When logout: I click the logout button
    Then logout: I should land on login page