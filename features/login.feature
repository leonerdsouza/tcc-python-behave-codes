@login
Feature: Login Validation

Scenario: Validate User Login
    Given I am at login page
    When I try to login
    Then I am logged in


