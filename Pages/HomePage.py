from selenium.webdriver.common.by import By


class HomePage:
    LOGIn_LNK = (By.CLASS_NAME, "login")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.find_element(*self.LOGIn_LNK).click()
