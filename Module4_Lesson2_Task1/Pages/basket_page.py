from .base_page import BasePage
from .locators import BasketPageLocators
from .data_language_dictionary import LANGUAGES_DICT


class BasketPage(BasePage):
    def __init__(self, browser, timeout=10):
        super().__init__(browser, timeout)
        self.browser = browser
        self.url = "http://selenium1py.pythonanywhere.com/basket/"
        self.browser.implicitly_wait(timeout)

    def should_not_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.products_in_basket), "The product is in the basket, but it shouldn't be"

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(BasketPageLocators.empty_basket_message).text
        assert LANGUAGES_DICT[self.browser.user_language]['empty_basket'] in message, "Empty basket message is not, but should be."