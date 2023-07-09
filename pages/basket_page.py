from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_products_in_basket()
        self.should_be_message_no_products()

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are some products in the basket."

    def should_be_message_no_products(self):
        msg = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert msg == "Your basket is empty. Continue shopping", "Basket is not empty."
