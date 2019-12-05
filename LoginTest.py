from selenium import webdriver


class LoginTest:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="set your chrome path here")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")

    def test_login(self, username, password):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(password)
        self.driver.find_element_by_id("SubmitLogin").click()

    def tearDown(self):
        self.driver.quit()


loginTest = LoginTest()
loginTest.setup()
loginTest.test_login("tst1.automation@gmail.com", "Test0001")
loginTest.tearDown()
