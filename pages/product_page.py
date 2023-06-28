from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def click_add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_be_basket_form_after_add_product(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_INFO_FORM), "Basket form is not presented when " \
                                                                               "the product added"

    def should_be_similar_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_from_form = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_FORM).text
        assert product_price == price_from_form, f"Prices are different: product price = '{product_price}' and price " \
                                                 f"from form = '{price_from_form}'"

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

    def should_be_message_with_book_name_form_after_add_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_FORM), "Add form with book's name is not " \
                                                                                 "presented when the product added"

    def should_be_similar_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_from_form = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_FORM).text
        assert product_name == name_from_form, f"Names are different: product name = '{product_name}' and name " \
                                               f"from form = '{name_from_form}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_FORM), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_FORM), \
            "Success message is presented, but should disappear"
