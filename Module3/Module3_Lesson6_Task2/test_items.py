from selenium.webdriver.common.by import By
import time

def test_should_present_button_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert (browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed()), "На странице нет кнопки добавления товара в корзину"