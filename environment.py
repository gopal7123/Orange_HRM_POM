import json
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.Login_Page import Login


def before_all(context):
    with open('Test_Data.json') as f:
        context.test_data = json.load(f)
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.login = Login(context.driver)

def after_step(context, step):
    if step.status == "failed":
        screenshot = context.driver.get_screenshot_as_png()
        allure.attach(screenshot, step.name, attachment_type=AttachmentType.PNG)


def before_step(context, step):
    print()


def after_all(context):
    context.driver.quit()


