from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import HTMLReport


class MiniBrute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_position(2000, 0)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    # @classmethod
    # def setUp(self):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login(self):   # Only bad combinations
        self.driver.get("https://opensource-demo.orangehrmlive.com/")


        with open("logins_bad.txt", "r") as file:
            logins = file.readlines()
        with open("passwords_bad.txt", "r") as file:
            passwords = file.readlines()

        for attempt in range(0, len(logins)):
            login_field = self.driver.find_element_by_id("txtUsername")
            password_field = self.driver.find_element_by_id("txtPassword")
            login_field.send_keys(logins[attempt])
            password_field.send_keys(passwords[attempt])
            self.driver.find_element_by_id("btnLogin").click()

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "txtUsername")))


if __name__ == '__main__':
    print("main")

    unittest.main(testRunner=HTMLReport.TestRunner(
        report_file_name="Report_Orange",
        output_path="./Reports",
        lang="en"
    ))
