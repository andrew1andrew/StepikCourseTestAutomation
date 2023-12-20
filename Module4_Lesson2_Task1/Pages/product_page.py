from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_shopping_cart(self):
        self.element_is_visible(ProductPageLocators.ADD_TO_THE_SHOPPING_CART).click()
        self.solve_quiz_and_get_code()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_THE_SHOPPING_CART), "Button is not presented"

    def check_product_and_basket_price(self):
        bookName = self.browser.find_element(ProductPageLocators.BOOK_NAME)
        bookPrice = self.browser.find_element(ProductPageLocators.BOOK_PRICE)
        bookNameBasket = self.browser.find_element(ProductPageLocators.BOOK_NAME_IN_BASKET)
        bookPriceBasket = self.browser.find_element(ProductPageLocators.BOOK_PRICE_IN_BASKET)
        errorTextMass = "Expected: '" + bookName.text + "' " + bookPrice.text + ". But got '" + bookNameBasket.text + "' " + bookPriceBasket.text
        assert (bookName.text == bookNameBasket.text) & (
                    bookPrice.text == bookPriceBasket.text), "ERROR: " + errorTextMass

    def should_not_be_success_message(self):
        assert self.is_element_present(ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"