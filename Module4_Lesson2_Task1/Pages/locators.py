from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[id='login_link']")

class ProductPageLocators:
    ADD_TO_THE_SHOPPING_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")