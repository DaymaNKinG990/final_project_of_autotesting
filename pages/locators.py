from selenium.webdriver.common.by import By


class MainPageLocators():
    # Login url
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Sing in\ Login
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    EMAIL_SING_IN = (By.CSS_SELECTOR, 'input#id_login-username.form-control')
    PASS_SING_IN = (By.CSS_SELECTOR, 'input#id_login-password.form-control')
    BTN_SING_IN = (By.CSS_SELECTOR, 'form#login_form > button.btn.btn-lg.btn-primary')

    # Sing up\Registration
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    EMAIL_SING_UP = (By.CSS_SELECTOR, 'input#id_registration-email.form-control')
    PASS_SING_UP_1 = (By.CSS_SELECTOR, 'input#id_registration-password1.form-control')
    PASS_SING_UP_2 = (By.CSS_SELECTOR, 'input#id_registration-password2.form-control')
    BTN_SING_UP = (By.CSS_SELECTOR, 'form#register_form > button.btn.btn-lg.btn-primary')


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_ADDED = (By.CSS_SELECTOR, 'div.alertinner')
    NAME_OF_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')