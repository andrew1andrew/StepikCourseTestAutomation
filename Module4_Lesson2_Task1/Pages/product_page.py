from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_product_to_the_shopping_cart(self):
        self.element_is_visible(ProductPageLocators.ADD_TO_THE_SHOPPING_CART).click()

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

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def disappear_of_success_message(self):
        assert self.is_disappeared(ProductPageLocators.SUCCESS_MESSAGE), "Success message isn't disappear"

    def product_name_on_page(self):
        return self.browser.find_element(ProductPageLocators.PRODUCT_NAME_ON_PAGE).text

    def product_price_on_page(self):
        return self.browser.find_element(ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text

    def check_alert_add_to_basket_name(self, expected_text_with_name):
        alerts_list = self.browser.find_elements(ProductPageLocators.PRODUCT_WAS_ADDED_SUCCESS_ALERT)
        assert len(alerts_list) > 0, "Error. Not alerts about basket."
        alerts_text = [x.text.rstrip() for x in alerts_list]
        assert expected_text_with_name in alerts_text, "Wrong name or message about adding in basket."

    def check_alert_add_to_basket_price(self, expected_price):
        alert = self.browser.find_element(ProductPageLocators.PRODUCT_WAS_ADDED_INFO_ALERT).text
        assert expected_price in alert, "Wrong price or message about adding in basket."

    def go_to_basket_page(self):
        link = self.browser.find_element(BasePageLocators.basket_link)
        link.click()