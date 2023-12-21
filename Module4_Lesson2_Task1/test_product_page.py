from Pages.product_page import ProductPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.basket_page import BasketPage
import time
import pytest
from Pages.data_language_dictionary import LANGUAGES_DICT


class TestProductPage:

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = MainPage(browser, link)
        page.open_page()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_product_to_the_shopping_cart()
        product_page.solve_quiz_and_get_code()
        product_page.check_product_and_basket_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_page()
        page.add_product_to_the_shopping_cart()
        # page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_page()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_page()
        page.add_product_to_the_shopping_cart()
        page.disappear_of_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_page()
        page.go_to_basket_page()
        basket_page = BasketPage(browser)
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open_page()
        main_page = MainPage(browser, link)
        main_page.check_go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_login_page()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser)
        page.open_page()
        email = str(time.time()) + "@mailforspam.org"
        page.register_new_user(email, "qwe123asd")
        page.should_be_authorized_user()
        yield

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = ProductPage(browser, link)
        page.open_page()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open_page()
        product_name = page.product_name_on_page()
        product_price = page.product_price_on_page()
        page.add_product_to_the_shopping_cart()
        template_name = LANGUAGES_DICT[page.browser.user_language]['add_to_basket_alert_with_name'].format(product_name)
        page.check_alert_add_to_basket_name(template_name)
        page.check_alert_add_to_basket_price(product_price)