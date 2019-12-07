from selenium.webdriver.common.by import By
from Data.UserDataBean import UserDataBean

class RegisterPage:
    EMAIL_ADRESS_INPUT = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")
    LOGIN_BTN = (By.ID, "SubmitLogin")

    def __init__(self, driver):
        self.driver = driver

    user_info = UserDataBean().random_user_data()

    def navigate_to_registration_page(self, username, password):
        self.driver.find_element(*self.EMAIL_ADRESS_INPUT).send_keys(self.user_info['email'])
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
