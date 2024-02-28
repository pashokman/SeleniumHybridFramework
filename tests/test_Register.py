from datetime import datetime
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestRefister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()     
        account_success_page = register_page.fill_register_form_mandatory_fields("John", "Doe", self.generate_email_with_timestamp(), '1234567890', '12345', 'no', 'select')
    
        expected_account_created_message = 'Your Account Has Been Created!'
        resulted_account_created_message = account_success_page.retrive_account_created_message()
        assert resulted_account_created_message == expected_account_created_message, "Account created messages (mandatory fields) does not match"


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()         
        account_success_page = register_page.fill_register_form_mandatory_fields("John", "Doe", self.generate_email_with_timestamp(), '1234567890', '12345', 'yes', 'select')
    
        expected_account_created_message = 'Your Account Has Been Created!'
        resulted_account_created_message = account_success_page.retrive_account_created_message()
        assert resulted_account_created_message == expected_account_created_message, "Account create messages (all fields) does not match"


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()        
        # email should be copied from test_Login.py - test_login_with_valid_credentials and email should be 
        # already registered another fields should be different from test_Login.py - test_login_with_valid_credentials
        register_page.fill_register_form_mandatory_fields("Jane", "Doe", 'test_auto@gmail.com', '2234567890', '123456', 'no', 'select')

        expected_duplicate_email_warning = 'Warning: E-Mail Address is already registered!'
        resulted_duplicate_email_warning = register_page.retrive_warning()
        assert resulted_duplicate_email_warning == expected_duplicate_email_warning, "Email err messages does not match"


    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()        
        register_page.fill_register_form_mandatory_fields('', '', '', '', '', 'no', 'no')

        expected_privacy_policy_warning = 'Warning: You must agree to the Privacy Policy!'
        expected_firstname_err_message = 'First Name must be between 1 and 32 characters!'
        expected_lastname_err_message = 'Last Name must be between 1 and 32 characters!'
        expected_email_err_message = 'E-Mail Address does not appear to be valid!'
        expected_telephone_err_message = 'Telephone must be between 3 and 32 characters!'
        expected_password_err_message = 'Password must be between 4 and 20 characters!'
        assert register_page.verify_all_warnings(expected_privacy_policy_warning, expected_firstname_err_message, expected_lastname_err_message, expected_email_err_message, expected_telephone_err_message, expected_password_err_message), "Register warning/message does not match"
        


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address