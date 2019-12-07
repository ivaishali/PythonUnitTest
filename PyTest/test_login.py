import pytest
from selenium import webdriver


class TestLoginPyTest:

    @pytest.fixture()
    def test_classMethods(self):
        self.driver = webdriver.Chrome(executable_path="/Users/vaishali.thakkar/ToDo/PythonUnitTest/chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        yield
        self.driver.quit()

    def test_login(self, test_classMethods, username="tst1.automation@gmail.com", password="Test0001"):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(password)
        self.driver.find_element_by_id("SubmitLogin").click()
