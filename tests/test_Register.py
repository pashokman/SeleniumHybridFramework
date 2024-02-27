from datetime import datetime
import pytest
from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRefister:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()        
        register_page.fill_register_form_mandatory_fields("John", "Doe", self.generate_email_with_timestamp(), 1234567890, 12345)
        register_page.accept_user_agreement()
        account_success_page = register_page.click_on_continue_btn()
    
        expected_account_created_message = 'Your Account Has Been Created!'
        resulted_account_created_message = account_success_page.retrive_account_created_message()
        assert resulted_account_created_message == expected_account_created_message, "Account created messages (mandatory fields) does not match"


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()        
        register_page.fill_register_form_mandatory_fields("John", "Doe", self.generate_email_with_timestamp(), 1234567890, 12345)
        register_page.accept_user_agreement()
        register_page.select_newsletter_radio_btn_no()
        account_success_page = register_page.click_on_continue_btn()
    
        expected_account_created_message = 'Your Account Has Been Created!'
        resulted_account_created_message = account_success_page.retrive_account_created_message()
        assert resulted_account_created_message == expected_account_created_message, "Account create messages (all fields) does not match"


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()        
        # email should be copied from test_Login.py - test_login_with_valid_credentials and email should be 
        # already registered another fields should be different from test_Login.py - test_login_with_valid_credentials
        register_page.fill_register_form_mandatory_fields("Jane", "Doe", 'test_auto@gmail.com', 2234567890, 123456)
        register_page.accept_user_agreement()
        register_page.click_on_continue_btn()

        expected_duplicate_email_warning = 'Warning: E-Mail Address is already registered!'
        resulted_duplicate_email_warning = register_page.retrive_warning()
        assert resulted_duplicate_email_warning == expected_duplicate_email_warning, "Email err messages does not match"


    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()        
        register_page.click_on_continue_btn()

        expected_privacy_policy_warning = 'Warning: You must agree to the Privacy Policy!'
        resulted_privacy_policy_warning = register_page.retrive_warning()
        assert resulted_privacy_policy_warning == expected_privacy_policy_warning, "Privacy policy messages does not match"
        
        expected_firstname_err_message = 'First Name must be between 1 and 32 characters!'
        resulted_firstname_err_message = register_page.retrive_firstname_err_message()
        assert resulted_firstname_err_message == expected_firstname_err_message, "Firstname err messages does not match"
        
        expected_lastname_err_message = 'Last Name must be between 1 and 32 characters!'
        resulted_lastname_err_message = register_page.retrive_lastname_err_message()
        assert resulted_lastname_err_message == expected_lastname_err_message, "Lastname err messages does not match"
        
        expected_email_err_message = 'E-Mail Address does not appear to be valid!'
        resulted_email_err_message = register_page.retrive_email_err_message()
        assert resulted_email_err_message == expected_email_err_message, "Email err messages does not match"
        
        expected_telephone_err_message = 'Telephone must be between 3 and 32 characters!'
        resulted_telephone_err_message = register_page.retrive_telephone_err_message()
        assert resulted_telephone_err_message == expected_telephone_err_message, "Telephone err messages does not match"
        
        expected_password_err_message = 'Password must be between 4 and 20 characters!'
        resulted_password_err_message = register_page.retrive_password_err_message()
        assert resulted_password_err_message == expected_password_err_message, "Password err messages does not match"


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address