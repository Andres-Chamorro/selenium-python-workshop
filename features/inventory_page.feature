Feature: Inventory Page Interaction
   Scenario: Verify Inventory Page Buttons are Displayed and Clickable
      Given the user is on the Inventory Page with items
      When the user clicks on both inventory item buttons
      Then the first inventory item button should be displayed
