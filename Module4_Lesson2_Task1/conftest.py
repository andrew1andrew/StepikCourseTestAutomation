from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def browser():
    service = Service()
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()