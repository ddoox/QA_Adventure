from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = "welcome"

    def check_logged(self):
        try:
            self.assertNotEqual("Welcome Admin", self.driver.find_element_by_id("welcome").text)
            self.driver.ass
        except NoSuchElementException:
            return 404



