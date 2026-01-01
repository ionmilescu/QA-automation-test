from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self,username):
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,"username"))).send_keys(username)
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_all_elements_located((By.ID,"password"))).send_keys(password)
    
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "loginBtn"))).click()