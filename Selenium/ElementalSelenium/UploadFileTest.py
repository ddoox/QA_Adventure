from selenium import webdriver
import unittest
import os
import HTMLReport
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UploadFileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_position(2000, 0)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @classmethod
    def test_00_upload_file(self):
        self.driver.get("http://the-internet.herokuapp.com/upload")
        file = open("../README.md")
        path = os.path.realpath("../README.md")
        filename = os.path.basename("../README.md")
        file.close()
        self.driver.find_element_by_id("file-upload").send_keys(path)
        self.driver.find_element_by_id("file-submit").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "uploaded-files")))
        result = self.driver.find_element_by_id("uploaded-files").text
        print(result)
        print(filename)
        # self.assertTrue(expected_conditions.presence_of_element_located(By.ID, ""))
        assert result == filename
        # self.assertEqual(result, filename)
        # self.assertEqual(result, filename)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLReport.TestRunner(
        report_file_name="Report_Upload",
        output_path="../../Reports",
        lang="en"
    ))