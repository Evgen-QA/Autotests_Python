from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', [*[f"?promo=offer{num}" for num in range(7)],              # 0-6
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),   # 7
                                  *[f"?promo=offer{num}" for num in range(8, 10)]])         # 8-9
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_basket_form_after_add_product()
    page.should_be_similar_price()
    page.should_be_message_with_book_name_form_after_add_product()
    page.should_be_similar_name()
