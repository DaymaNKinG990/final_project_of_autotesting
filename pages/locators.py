from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
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


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_ADDED = (By.CSS_SELECTOR, 'div.alertinner > strong')
    NAME_OF_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner > p')
    BASKET_FORM = (By.CSS_SELECTOR, '.basket-items')
