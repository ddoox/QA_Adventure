from selenium.common.exceptions import NoSuchElementException
from OrangeHRM.Locators.Locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
