Feature: Delete Product from Inventory
   Scenario: Add a product to the inventory and then remove it from the cart
    Given the user has added a product to the Inventory Page
    When the user navigates to the cart page
    And the user clicks on the delete product button
    Then the product should be removed from the inventory list
