import pytest
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginPyTestPOM:
    testdata = [
        ("tst1.automation@gmail.com", "Test0001"),
        ("tst1.automation@gmail.com", "Test0001"),
    ]

    @pytest.fixture()
    def test_classMethods(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path="../Driver/chromedriver")
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        yield
        self.driver.quit()

    def test_login(self, test_classMethods, username="tst1.automation@gmail.com", password="Test0001"):
        homePage = HomePage(self.driver)
        homePage.navigate_to_login_page()

        loginPage = LoginPage(self.driver)
        loginPage.login(username, password)

    @pytest.fixture
    def login_credentials(self):
        return ['tst1.automation@gmail.co', 'Test0001']
