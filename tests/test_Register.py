from datetime import datetime
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestRefister:
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address


    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        
        self.driver.find_element(By.NAME, 'firstname').send_keys("John")
        self.driver.find_element(By.NAME, 'lastname').send_keys("Doe")
        self.driver.find_element(By.NAME, 'email').send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.NAME, 'telephone').send_keys(1234567890)
        self.driver.find_element(By.NAME, 'password').send_keys(12345)
        self.driver.find_element(By.NAME, 'confirm').send_keys(12345)
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

        expected_account_create_message = 'Your Account Has Been Created!'
        resulted_account_create_message = self.driver.find_element(By.XPATH, '//div[@id="content"]/h1').text
        assert resulted_account_create_message == expected_account_create_message, "Account create messages (mandatory fields) does not match"


    def test_register_with_all_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        
        self.driver.find_element(By.NAME, 'firstname').send_keys("John")
        self.driver.find_element(By.NAME, 'lastname').send_keys("Doe")
        self.driver.find_element(By.NAME, 'email').send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.NAME, 'telephone').send_keys(1234567890)
        self.driver.find_element(By.NAME, 'password').send_keys(12345)
        self.driver.find_element(By.NAME, 'confirm').send_keys(12345)
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="0"]').click()
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

        expected_account_create_message = 'Your Account Has Been Created!'
        resulted_account_create_message = self.driver.find_element(By.XPATH, '//div[@id="content"]/h1').text
        assert resulted_account_create_message == expected_account_create_message, "Account create messages (all fields) does not match"


    def test_register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        
        self.driver.find_element(By.NAME, 'firstname').send_keys("John")
        self.driver.find_element(By.NAME, 'lastname').send_keys("Doe")
        # email should be copied from test_Login.py - test_login_with_valid_credentials and should be already registered
        self.driver.find_element(By.NAME, 'email').send_keys('test_auto@gmail.com')
        self.driver.find_element(By.NAME, 'telephone').send_keys(1234567890)
        self.driver.find_element(By.NAME, 'password').send_keys(12345)
        self.driver.find_element(By.NAME, 'confirm').send_keys(12345)
        self.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="0"]').click()
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

        expected_email_registered_err_message = 'Warning: E-Mail Address is already registered!'
        resulted_email_registered_err_message = self.driver.find_element(By.XPATH, '//div[@id="account-register"]/div[1]').text
        assert resulted_email_registered_err_message == expected_email_registered_err_message, "Email err messages does not match"


    def test_register_without_entering_any_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

        expected_privacy_policy_err_message = 'Warning: You must agree to the Privacy Policy!'
        resulted_privacy_policy_err_message = self.driver.find_element(By.XPATH, '//div[@id="account-register"]/div[1]').text
        assert resulted_privacy_policy_err_message == expected_privacy_policy_err_message, "Privacy policy messages does not match"
        
        expected_first_name_err_message = 'First Name must be between 1 and 32 characters!'
        resulted_first_name_err_message = self.driver.find_element(By.XPATH, '//input[@name="firstname"]/following-sibling::div').text
        assert resulted_first_name_err_message == expected_first_name_err_message, "First name err messages does not match"
        
        expected_last_name_err_message = 'Last Name must be between 1 and 32 characters!'
        resulted_last_name_err_message = self.driver.find_element(By.XPATH, '//input[@name="lastname"]/following-sibling::div').text
        assert resulted_last_name_err_message == expected_last_name_err_message, "Last name err messages does not match"
        
        expected_email_err_message = 'E-Mail Address does not appear to be valid!'
        resulted_email_err_message = self.driver.find_element(By.XPATH, '//input[@name="email"]/following-sibling::div').text
        assert resulted_email_err_message == expected_email_err_message, "Email err messages does not match"
        
        expected_telephone_err_message = 'Telephone must be between 3 and 32 characters!'
        resulted_telephone_err_message = self.driver.find_element(By.XPATH, '//input[@name="telephone"]/following-sibling::div').text
        assert resulted_telephone_err_message == expected_telephone_err_message, "Telephone err messages does not match"
        
        expected_password_err_message = 'Password must be between 4 and 20 characters!'
        resulted_password_err_message = self.driver.find_element(By.XPATH, '//input[@name="password"]/following-sibling::div').text
        assert resulted_password_err_message == expected_password_err_message, "Password err messages does not match"
