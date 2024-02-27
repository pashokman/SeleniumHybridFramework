from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver


    field_after_successful_login_link_text = 'Edit your account information'


    def display_status_of_field_after_successful_login(self):
        return self.driver.find_element(By.LINK_TEXT, self.field_after_successful_login_link_text).is_displayed()