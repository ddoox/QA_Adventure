from selenium import webdriver
from OrangeHRM.Pages.LoginPage import LoginPage
import pytest


@pytest.fixture()
def test_setup():
    global driver
    # driver = webdriver.Chrome("../../drivers/chromedriver")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/logout")
    yield   # teardown
    driver.close()


def test_login(test_setup):
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    title = driver.title
    assert title == "OrangeHRM"

#
# def teardown():
#     driver.close()
