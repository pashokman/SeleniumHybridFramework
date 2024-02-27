from datetime import datetime
import pytest
from pages.AccountPage import AccountPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        # create by hands a new account for testing with the same credentials or change them
        login_page = LoginPage(self.driver)
        login_page.enter_email_address('test_auto@gmail.com')
        login_page.enter_password('12345')
        login_page.click_login_btn()

        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_field_after_successful_login(), "Successful login failed"


    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        # a new email address is generated every time
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_timestamp())
        login_page.enter_password('12345')
        login_page.click_login_btn()

        expected_no_match_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_no_match_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_no_match_warning == expected_no_match_warning, "Email/Password warnings does not match"


    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        # create by hands a new account for testing with the same credentials or change them
        login_page = LoginPage(self.driver)
        login_page.enter_email_address('test_auto@gmail.com')
        login_page.enter_password('123456')
        login_page.click_login_btn()

        expected_error_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_error_warning == expected_error_warning, "Email/Password warnings does not match"


    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)
        login_page.click_login_btn()

        expected_error_warning = 'Warning: No match for E-Mail Address and/or Password.'
        resulted_error_warning = login_page.retrive_no_match_email_pwd()
        assert resulted_error_warning == expected_error_warning, "Email/Password warnings does not match"


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address