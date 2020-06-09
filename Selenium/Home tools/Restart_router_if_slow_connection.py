from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')  # Windows absolute
driver = webdriver.Firefox()

driver.get("http://192.168.1.1")
assert "TD-W8980" in driver.title
# assert "not ok" in driver.title

login = driver.find_element_by_id("userName")
login.clear()
login.send_keys("admin")

password = driver.find_element_by_id("pcPassword")
password.clear()
password.send_keys("admin")  # Just a placeholder ;)
password.send_keys(Keys.RETURN)

assert "TD-W8980" in driver.title

sleep(0.2)   # Was too fast

speed = driver.find_element_by_id("downstreamCurrRate")
print(speed.text)

if int(speed.text) < 15000:

    #   -   -   -   Reboot  -   -   -   #
    link = driver.find_element_by_id("menu_tools")
    link.click()

    link = driver.find_element_by_id("menu_restart")
    link.click()

    button = driver.find_element_by_id("button_reboot")
    button.click()

    alert = driver.switch_to.alert
    alert.accept()

driver.close()
