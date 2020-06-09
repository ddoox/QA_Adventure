from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest



class MyTest(unittest.TestCase):
    # def setUp(self)           before each test
    # def setUpClass(cls)       once for whole class
    # def tearDown(self)        after each test
    # def tearDownClass(cls)    once at the end of class

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

    def test_search_testv2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Testv2" + Keys.RETURN)


if __name__ == '__main__':
    unittest.main()
