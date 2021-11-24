@site
Feature: Site Validation

Scenario: Validate User Purchase
    Given I am at home page
    When I login into the site
    Then I am logged at Products page
    And I click on Sauce Labs Backpack
    And I add the item to the shopping cart
    And I click on the cart button
    Then I proceed to checkout the product
    And I fill in the Personal Information
    Then I should see the overview page
    And I click on the finish button
    Then I  should see the order has been completed 



