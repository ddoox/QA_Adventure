from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest
import HTMLReport
from OrangeHRM.Pages.LoginPage import LoginPage
from OrangeHRM.Locators.Locators import Locators


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../../drivers/chromedriver")
        # cls.driver = webdriver.Firefox()
        cls.driver.set_window_position(2000, 0)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @classmethod
    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/logout")

    def test_99_bad_logins(self):   # Only bad combinations + a few SQLi
        with open("../Data/logins_bad.txt", "r") as file:
            logins = file.readlines()
        with open("../Data/passwords_bad.txt", "r") as file:
            passwords = file.readlines()

        for attempt in range(0, len(logins)):
            login = LoginPage(self.driver)
            login.enter_username(logins[attempt])
            login.enter_password(passwords[attempt])
            login.click_login()
            try:
                self.assertNotEqual("Welcome Admin", self.driver.find_element_by_id(Locators.password_textbox_id).text)
            except NoSuchElementException:
                continue

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
