from datetime import datetime
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        # create by hands a new account for testing with the same credentials or change them
        self.driver.find_element(By.NAME, 'email').send_keys('test_auto@gmail.com')
        self.driver.find_element(By.NAME, 'password').send_keys('12345')
        self.driver.find_element(By.XPATH, '//input[@value="Login"]').click()

        assert self.driver.find_element(By.LINK_TEXT, 'Edit your account information').is_displayed()


    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        # a new email address is generated every time
        self.driver.find_element(By.NAME, 'email').send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.NAME, 'password').send_keys('12345')
        self.driver.find_element(By.XPATH, '//input[@value="Login"]').click()

        expected_error_message = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_message = self.driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
        assert resulted_error_message == expected_error_message, "Email/Password err messages does not match"


    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        # create by hands a new account for testing with the same credentials or change them
        self.driver.find_element(By.NAME, 'email').send_keys('test_auto@gmail.com')
        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        self.driver.find_element(By.XPATH, '//input[@value="Login"]').click()

        expected_error_message = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_message = self.driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
        assert resulted_error_message == expected_error_message, "Email/Password err messages does not match"


    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        self.driver.find_element(By.XPATH, '//input[@value="Login"]').click()

        expected_error_message = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_message = self.driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
        assert resulted_error_message == expected_error_message, "Email/Password err messages does not match"


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address