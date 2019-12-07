from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Demo:
    def setup(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path="../Driver/chromedriver")
        self.driver.get("https://github.com/SergeyPirogov/webdriver_manager")
Demo().setup()