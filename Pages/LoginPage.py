from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    LOGIN_BTN = (By.ID, "SubmitLogin")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
