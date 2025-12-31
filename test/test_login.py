from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


def test_valid_login():
    driver = webdriver.Chrome (service = Service(ChromeDriverManager().install()))
    driver.get("http:example.com/login")

    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()

    driver.quit()