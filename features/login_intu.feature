Feature: Intu Login Feature
    Scenario: Successfull intu Login
       Given the user is in the intu login page
       When the user logs in with valid intu credentials
       Then the user should be redirected to the dashboard page
       