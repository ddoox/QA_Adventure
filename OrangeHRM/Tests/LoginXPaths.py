from selenium import webdriver
import unittest
import HTMLReport
from OrangeHRM.Pages.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        print("text(): " + self.driver.find_element_by_xpath("//a[text()=\"Welcome Admin\"]").text)
        print("contains(): " + self.driver.find_element_by_xpath('//a[contains(text(), "Admin")]').text)
        print("starts-with(): " + self.driver.find_element_by_xpath('//a[starts-with(text(), "Wel")]').text)
        print("or: " + self.driver.find_element_by_xpath('//a[starts-with(text(), "Wel") or @id="placeholder"]').text)
        # print("and: " + self.driver.find_element_by_xpath('//a[starts-with(text(), "Wel") and @id="placeholder"]').text)
        print("and: " + self.driver.find_element_by_xpath('//a[starts-with(text(), "Wel") and @href="#"]').text)
        self.assertEqual("Welcome Admin", self.driver.find_element_by_xpath("//a[@id=\"welcome\"]").text)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLReport.TestRunner(
        report_file_name="Report_Orange",
        output_path="../../Reports",
        lang="en"
    ))
