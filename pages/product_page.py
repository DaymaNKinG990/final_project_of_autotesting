from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):

    def adding_item_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_visible_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), 'Button not found'

    def item_added_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text == self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED), \
            "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED), \
            "Success message is disappeared"
