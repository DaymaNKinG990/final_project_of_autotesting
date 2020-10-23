import pytest
import time
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.user_adding_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/')
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()) + "pa33w0rd")
        self.page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_be_visible_button()
        self.page.adding_item_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.item_added_to_basket()
        self.page.should_be_disappear()

    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_basket_is_empty()
