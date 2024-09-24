Feature: Login functionality of OrangeHRM

  Scenario: Login to OrangeHRM
    Given navigate to the login page at "url"
    When enter the username "username" and the password "password"
    And click the login button
    Then should be successfully logged in

#  Scenario: Dashboard Access
#    Then should be redirected to the dashboard
#    And verify that the dashboard is displayed

  Scenario: Logout from OrangeHRM
    When click on the profile dropdown
    And click on the logout button
