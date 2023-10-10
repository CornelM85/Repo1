Feature: Login Capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click the login button


  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "Cornel" and password "Cornel12#$"
    Then books: I should land on books page


  @regression
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and password "<pswd>"
    Then login: I validate that error message is displayed

  Examples:
    | user   | pswd     |
    | Cornel | Cornel12 |
    | Cornel | sadasdsa |






