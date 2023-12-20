from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_elements(By.TAG_NAME, "input")
    first_name[0].send_keys("Andrew")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Zheleznyak")
    email = browser.find_element(By.CLASS_NAME, "form-control.third")
    email.send_keys("test@mail.ru")
    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    phone.send_keys("89995554433")
    address = browser.find_elements(By.CSS_SELECTOR, "[maxlength='32']")
    address[4].send_keys("Lenina 5")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    registration_message = browser.find_element(By.TAG_NAME, "h1").text
    assert registration_message == "Congratulations! You have successfully registered!"
finally:
    time.sleep(5)
    browser.quit()