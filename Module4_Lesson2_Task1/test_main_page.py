from Pages.main_page import MainPage
from Pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"
class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open_page()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open_page()
        page.should_be_login_link()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open_page()
        page.check_go_to_login_page()
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open_page()
        page.should_be_login_link()
