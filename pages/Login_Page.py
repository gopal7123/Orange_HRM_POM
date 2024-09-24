from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Login():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # login page locators
    username_textbox_name   = "username"
    password_textbox_name   = "password"
    login_button_xpath      = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalid_cred_text_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
    invalid_text_xpath      = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'

    def enter_username(self, username):
      self.driver.find_element(By.NAME, self.username_textbox_name).clear()
      self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
      self.driver.find_element(By.NAME, self.password_textbox_name).clear()
      self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
      self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_cred_text(self):
      txt = self.driver.find_element(By.XPATH, self.invalid_text_xpath).text
      if txt == "Invalid credentials":
        assert True, f"Invalid credentials Text verified"
      else:
        assert False, f"Invalid credentials Text not find"

    def enter_txt_field(self, element, txt_value):
        self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).send_keys(txt_value)

    def click_btn_js(self, element):
        Btn = self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0])))
        self.driver.execute_script("arguments[0].click();", Btn)

    def click_button(self, element):
        self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).click()

    def select_from_dropdown(self, locator, visible_text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def clear_element(self, element):
        self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).clear()

    def verify_labels(self, element, label):
        self.final_txt = self.wait.until(
            EC.presence_of_element_located((list(element.keys())[0], list(element.values())[0]))).text
        if self.final_txt == label:
            assert True, f"final_txt{self.final_txt}"
        else:
            assert False, f"exception occurred ---> {self.final_txt}"

    def get_element(self, element):
        return self.wait.until(EC.presence_of_element_located((list(element.keys())[0], list(element.values())[0])))

    def element_enabled(self, element):
        ele = self.wait.until(
            EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).is_enabled()
        if ele:
            assert True, f"element {ele} is present"
        else:
            assert False, f"element {ele} is absent"

    def element_selected(self,element):
        ele = self.wait.until(
            EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).is_selected()
        if ele:
            assert True, f"element {ele} is present"
        else:
            assert False, f"element {ele} is absent"

    def select_dynamic_option(self,element,visible_text):
        ele = self.wait.until(
            EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0])))
        select = Select(ele)
        options = select.options
        for var in options:
            if visible_text in var.text:
                select.select_by_visible_text(var.text)