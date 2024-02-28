from datetime import datetime
import pytest
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        # create by hands a new account for testing with the same credentials or change them
        account_page = login_page.login('test_auto@gmail.com', '12345')

        assert account_page.display_status_of_field_after_successful_login(), "Successful login failed"


    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        # a new email address is generated every time
        login_page.login(self.generate_email_with_timestamp(), '12345')
        
        expected_no_match_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_no_match_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_no_match_warning == expected_no_match_warning, "Email/Password warnings does not match"


    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        # create by hands a new account for testing with the same credentials or change them
        login_page.login('test_auto@gmail.com', '123456')
        
        expected_error_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_error_warning == expected_error_warning, "Email/Password warnings does not match"


    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login('', '')
        
        expected_error_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_error_warning == expected_error_warning, "Email/Password warnings does not match"


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address