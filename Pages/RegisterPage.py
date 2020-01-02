from selenium.webdriver.common.by import By
from Data.UserDataBean import UserDataBean
from selenium.webdriver.support.ui import Select


class RegisterPage:
    user_info = UserDataBean().get_random_string_start_with_uppercase()

    EMAIL_ADRESS_INPUT = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")

    # Account Creation elements screen
    TITILE_MR = (By.ID, "id_gender1")
    TITILE_MRS = (By.ID, "id_gender2")
    FIRSTNAME_INPUT = (By.ID, "customer_firstname")
    LASTNAME_INPUT = (By.ID, "customer_lastname")
    PASSWORD_INPUT = (By.ID, "passwd")
    DOB_DATE_SELECT = (By.ID, "days")
    DOB_MONTH_SELECT = (By.ID, "months")
    DOB_YEAR_SELECT = (By.ID, "years")

    ADD_FIRSTNAME_INPUT = (By.ID, "firstname")
    ADD_LASTNAME_INPUT = (By.ID, "lastname")
    ADD_COMPANY_INPUT = (By.ID, "company")
    ADD_ADDRESS_INPUT = (By.ID, "address1")
    ADD_CITY_INPUT = (By.ID, "city")
    ADD_ZIPCODE_INPUT = (By.ID, "postcode")
    ADD_MOBILENO_INPUT = (By.ID, "phone_mobile")
    ADD_STATE_DROPDOWN = (By.ID, "id_state")
    ADD_COUNTRY_DROPDOWN = (By.ID, "id_country")
    REGISTER_BTN = (By.ID, "submitAccount")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_registration_page(self, user_info):
        self.driver.find_element(*self.EMAIL_ADRESS_INPUT).send_keys(user_info['email'])
        self.driver.find_element(*self.CREATE_ACCOUNT_BTN).click()

    def selectFromDropDown(self, value, loc):
        dropDownElement = Select(loc)
        dropDownElement.select_by_value(value)

    def fill_registration_details(self, user_info):
        self.driver.find_element(*self.TITILE_MR).click()
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(user_info['firstname'])
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(user_info['lastname'])
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(user_info['password'])
        # self.driver.find_element(*self.TITILE_MR).send_keys("")
        # self.driver.find_element(*self.TITILE_MR).send_keys("")
        # self.driver.find_element(*self.TITILE_MR).send_keys("")
        # self.driver.find_element(*self.TITILE_MR).send_keys("")
