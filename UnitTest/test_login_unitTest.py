from selenium import webdriver
import unittest
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="D:\\Automation\\GitProject\\PythonUnitTest\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")

    def test_login(self, username="tst1.automation@gmail.com", password="Test0001"):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(password)
        self.driver.find_element_by_id("SubmitLogin").click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

