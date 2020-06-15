from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest
import HTMLReport
from Selenium.OrangeHRM.Pages.LoginPage import LoginPage
from Selenium.OrangeHRM.Locators.Locators import Locators
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver = webdriver.Chrome(GeckoDriverManager(path="/home/doox/PycharmProjects/Selenium/drivers").install())   # TODO: Check on Windows
        cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())        # Work
        # cls.driver = webdriver.Ie(IEDriverManager().install())              # Check on Windows - working
        # cls.driver = webdriver.Opera(OperaDriverManager(path="/home/doox/PycharmProjects/Selenium/drivers").install())
        # driver = webdriver.Opera(executable_path=OperaDriverManager(log_level=0).install())   # TODO: Check on Windows


        cls.driver.set_window_position(2000, 0)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    @classmethod
    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/logout")

    def test_02_correct_login(self):
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        self.assertEqual("Welcome Admin", self.driver.find_element_by_id("welcome").text)

    def test_03_bad_assert(self):
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        self.assertEqual("Welcome", self.driver.find_element_by_id("welcome").text)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLReport.TestRunner(
        report_file_name="Report_Orange",
        output_path="../../Reports",
        lang="en"
    ))
