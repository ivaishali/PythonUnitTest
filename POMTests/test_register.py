import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from webdriver_manager.chrome import ChromeDriverManager
from Data.UserDataBean import UserDataBean


class TestRegister:

    @pytest.yield_fixture()
    def testFixtures(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path="../Driver/chromedriver")
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        yield
        self.driver.quit()

    def test_Register(self, testFixtures):
        homePage = HomePage(self.driver)
        homePage.navigate_to_login_page()

        userInfo = UserDataBean().get_random_user_data()
        registerPage = RegisterPage(self.driver)
        registerPage.navigate_to_registration_page(userInfo)
        registerPage.fill_registration_details(userInfo)
