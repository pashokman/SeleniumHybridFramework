from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    field_firstname_name = 'firstname'
    field_lastname_name = 'lastname'
    field_email_name = 'email'
    field_telephone_name = 'telephone'
    field_password_name = 'password'
    field_confirm_pwd_name = 'confirm'
    field_agree_name = 'agree'
    radio_btn_yes_newsletter_xpath = '//input[@name="newsletter"][@value="1"]'
    continue_btn_xpath = '//input[@value="Continue"]'
    warning_xpath = '//div[@id="account-register"]/div[1]'
    firstname_err_message_xpath = '//input[@name="firstname"]/following-sibling::div'
    lastname_err_message_xpath = '//input[@name="lastname"]/following-sibling::div'
    email_err_message_xpath = '//input[@name="email"]/following-sibling::div'
    telephone_err_message_xpath = '//input[@name="telephone"]/following-sibling::div'
    password_err_message_xpath = '//input[@name="password"]/following-sibling::div'


    def enter_firstname(self, firstname):
        self.type_into_element('field_firstname_name', self.field_firstname_name, firstname)


    def enter_lastname(self, lastname):
        self.type_into_element('field_lastname_name', self.field_lastname_name, lastname)


    def enter_email(self, email):
        self.type_into_element('field_email_name', self.field_email_name, email)


    def enter_telephone(self, telephone):
        self.type_into_element('field_telephone_name', self.field_telephone_name, telephone)


    def enter_pwd_and_confirm_pwd(self, password):
        self.type_into_element('field_password_name', self.field_password_name, password)
        self.type_into_element('field_confirm_pwd_name', self.field_confirm_pwd_name, password)


    def fill_register_form_mandatory_fields(self, firstname, lastname, email, telephone, 
                                            password, newsletter_yes_or_no, privacy_policy):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_pwd_and_confirm_pwd(password)
        if newsletter_yes_or_no == 'yes':
            self.select_newsletter_radio_btn_yes()
        if privacy_policy == 'select':
            self.accept_user_agreement()
        return self.click_on_continue_btn()


    def accept_user_agreement(self):
        self.element_click('field_agree_name', self.field_agree_name)


    def select_newsletter_radio_btn_yes(self):
        self.element_click('radio_btn_yes_newsletter_xpath', self.radio_btn_yes_newsletter_xpath)


    def click_on_continue_btn(self):
        self.element_click('continue_btn_xpath', self.continue_btn_xpath)
        return AccountSuccessPage(self.driver)


    def retrive_warning(self):
        return self.retrive_element_text('warning_xpath', self.warning_xpath)
    

    def retrive_firstname_err_message(self):
        return self.retrive_element_text('firstname_err_message_xpath', self.firstname_err_message_xpath)
    

    def retrive_lastname_err_message(self):
        return self.retrive_element_text('lastname_err_message_xpath', self.lastname_err_message_xpath)
    

    def retrive_email_err_message(self):
        return self.retrive_element_text('email_err_message_xpath', self.email_err_message_xpath)
    

    def retrive_telephone_err_message(self):
        return self.retrive_element_text('telephone_err_message_xpath', self.telephone_err_message_xpath)
    
    
    def retrive_password_err_message(self):
        return self.retrive_element_text('password_err_message_xpath', self.password_err_message_xpath)
    

    def verify_all_warnings(self, expected_privacy_policy_warning, expected_firstname_err_message, 
                            expected_lastname_err_message, expected_email_err_message, 
                            expected_telephone_err_message, expected_password_err_message):
        actual_privacy_policy_warning = self.retrive_warning()
        actual_firstname_err_message = self.retrive_firstname_err_message()
        actual_lastname_err_message = self.retrive_lastname_err_message()
        actual_email_err_message = self.retrive_email_err_message()
        actual_telephone_err_message = self.retrive_telephone_err_message()
        actual_password_err_message = self.retrive_password_err_message()

        status = False
        if expected_privacy_policy_warning.__contains__(actual_privacy_policy_warning):
            if expected_firstname_err_message.__eq__(actual_firstname_err_message):
                if expected_lastname_err_message.__eq__(actual_lastname_err_message):
                    if expected_email_err_message.__eq__(actual_email_err_message):
                        if expected_telephone_err_message.__eq__(actual_telephone_err_message):
                            if expected_password_err_message.__eq__(actual_password_err_message):
                                status = True

        return status