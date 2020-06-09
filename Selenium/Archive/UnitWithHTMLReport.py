from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HTMLReport


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_position(2000, 0)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_search_unittests(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Unit Tests" + Keys.RETURN)

    def test_to_error(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("NO_NAME").send_keys("Unit Tests" + Keys.RETURN)

    def test_search_testv2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Testv2" + Keys.RETURN)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLReport.TestRunner(
        report_file_name="Report",
        output_path="../Reports",
        lang="en"
    ))
