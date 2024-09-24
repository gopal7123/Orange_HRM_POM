import time
from selenium import webdriver
from behave import *
from pages.Login_Page import Login
from pages.homepage import HomePage
from selenium.webdriver.common.by import By

@given(u'navigate to the login page at "{url}"')
def step_impl(context, url):
    url = context.test_data['login'][url]
    context.driver.get(url)


@when(u'enter the username "{username}" and the password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.NAME, Login.username_textbox_name).send_keys(context.test_data["login"][username])
    context.driver.find_element(By.NAME, Login.password_textbox_name).send_keys(context.test_data["login"][password])


@when(u'click the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, Login.login_button_xpath).click()
    time.sleep(5)


@then(u'should be successfully logged in')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH, HomePage.dashboard_text_xpath).text
    if txt == "Dashboard":
      assert True, f"{txt} present"
    else:
      assert False, f"{txt} not present"
    time.sleep(5)


@when(u'click on the profile dropdown')
def step_impl(context):
  homepage = HomePage(context.driver)  # Initialize the HomePage with the driver
  homepage.click_profile()  # Use the click_profile function


@when(u'click on the logout button')
def step_impl(context):
  time.sleep(2)
  homepage = HomePage(context.driver)  # Initialize the HomePage with the driver
  homepage.click_logout()  # Use the click_profile function
