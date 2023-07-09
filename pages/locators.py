from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_INFO_FORM = (By.CSS_SELECTOR, ".alert-info")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_FROM_FORM = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_ADDED_FORM = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_FROM_FORM = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")


class BasketPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group a.btn")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
