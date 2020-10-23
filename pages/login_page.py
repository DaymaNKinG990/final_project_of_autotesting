from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Can\'t find word login in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not found login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Not found register form'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_SING_UP)
        email_input.send_keys(email)
        pas_input_1 = self.browser.find_element(*LoginPageLocators.PASS_SING_UP_1)
        pas_input_1.send_keys(password)
        pas_input_2 = self.browser.find_element(*LoginPageLocators.PASS_SING_UP_2)
        pas_input_2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_SING_UP).click()
