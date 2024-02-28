from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)


    email_address_field_name = 'email'
    password_field_name = 'password'
    login_btn_xpath = '//input[@value="Login"]'
    no_match_email_pwd_warning_xpath = '//div[@id="account-login"]/div[1]'


    def enter_email_address(self, email_address):
        self.type_into_element('email_address_field_name', self.email_address_field_name, email_address)
    

    def enter_password(self, password):
        self.type_into_element('password_field_name', self.password_field_name, password)


    def click_login_btn(self):
        self.element_click('login_btn_xpath', self.login_btn_xpath)
        return AccountPage(self.driver)


    def retrive_no_match_email_pwd(self):
        return self.retrive_element_text('no_match_email_pwd_warning_xpath', self.no_match_email_pwd_warning_xpath)
    

    def login(self, email_address, password):
        self.enter_email_address(email_address)
        self.enter_password(password)
        return self.click_login_btn()
    