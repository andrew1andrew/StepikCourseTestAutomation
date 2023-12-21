from selenium.webdriver.common.by import By

class GeneralLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[id='login_link']")


class LoginPageLocators:
    form_login = (By.CSS_SELECTOR, "#login_form")
    place_email_address_locator = (By.CSS_SELECTOR, "[name='login-username']")
    place_password_locator = (By.CSS_SELECTOR, "[name='login-password']")
    button_login_locator = (By.CSS_SELECTOR, '[name="login_submit"]')
    form_register = (By.CSS_SELECTOR, "#register_form")
    place_registration_email_locator = (By.CSS_SELECTOR, '[name="registration-email"]')
    place_password_registration_locator = (By.CSS_SELECTOR, '[name="registration-password1"]')
    place_password_repead_locator = (By.CSS_SELECTOR, '[name="registration-password2"]')
    button_registration_locator = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_THE_SHOPPING_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_WAS_ADDED_SUCCESS_ALERT = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    PRODUCT_WAS_ADDED_INFO_ALERT = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")


class BasketPageLocators(GeneralLocators):
    empty_basket_message = (By.CSS_SELECTOR, "#content_inner")
    products_in_basket = (By.CSS_SELECTOR, "#basket_formset")


class BasePageLocators(GeneralLocators):
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")
    basket_link = (By.CSS_SELECTOR, "div.basket-mini span a.btn.btn-default")
    user_icon = (By.CSS_SELECTOR, ".icon-user")