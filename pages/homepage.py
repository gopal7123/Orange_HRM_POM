from selenium.webdriver.common.by import By


class HomePage():
  def __init__(self, driver):
    self.driver = driver

  # homepage locators
  dashboard_text_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'
  profile_dropdown_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i'
  logout_dropdown_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'

  def click_profile(self):
    self.driver.find_element(By.XPATH, self.profile_dropdown_xpath).click()

  def click_logout(self):
    self.driver.find_element(By.XPATH, self.logout_dropdown_xpath).click()

