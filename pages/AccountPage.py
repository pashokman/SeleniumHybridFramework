from pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    field_after_successful_login_link_text = 'Edit your account information'


    def display_status_of_field_after_successful_login(self):
        return self.check_display_status_of_element('field_after_successful_login_link_text', 
                                                    self.field_after_successful_login_link_text)