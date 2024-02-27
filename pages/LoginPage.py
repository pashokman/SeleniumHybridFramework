from selenium.webdriver.common.by import By


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver

    email_address_field_name = 'email'
    password_field_name = 'password'
    login_btn_xpath = '//input[@value="Login"]'
    no_match_email_pwd_warning_xpath = '//div[@id="account-login"]/div[1]'


    def enter_email_address(self, email_address):
        self.driver.find_element(By.NAME, self.email_address_field_name).click()
        self.driver.find_element(By.NAME, self.email_address_field_name).clear()
        self.driver.find_element(By.NAME, self.email_address_field_name).send_keys(email_address)
    

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_name).click()
        self.driver.find_element(By.NAME, self.password_field_name).clear()
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password)


    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()


    def retrive_no_match_email_pwd(self):
        return self.driver.find_element(By.XPATH, self.no_match_email_pwd_warning_xpath).text