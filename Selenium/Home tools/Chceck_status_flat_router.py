import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep


password_value = "admin"  # ;)

driver = webdriver.Firefox()
driver.set_window_position(2000, 0)
driver.maximize_window()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipv4 = s.getsockname()[0]
s.close()

ipv4 = ipv4.split(".")
ipv4[3] = "1"  # /24
ipv4 = ".".join(ipv4)
print(ipv4)


driver.get("http://" + ipv4)

# slow GUI
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.ID, "loginPassword")))

password = driver.find_element_by_name("loginPassword")
password.send_keys(password_value)
password.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.ID, "c_hp02")))

diag = driver.find_element_by_id("c_hp02")
diag.click()

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "c_dn01")))

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "running_scope")))

diag_complete = driver.find_element_by_id("diag_complete")
while driver.find_element_by_id("running_scope"):
    percent = driver.find_element_by_id("percent").text
    print("diag: " + percent)
    sleep(1)
    if diag_complete.value_of_css_property("display") == "block":
        break

diag_text = driver.find_element_by_id("c_dn01").text

print("result = " + diag_text)

if diag_text != "Połączenie z siecią Internet działa prawidłowo.":
    close_button = driver.find_element_by_id("c_51")
    close_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "c_mu25")))
    admin_tools_button = driver.find_element_by_id("c_mu25")
    admin_tools_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "c_mu27")))
    restart_menu_button = driver.find_element_by_id("c_mu27")
    restart_menu_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "c_rr14")))
    restart_router_button = driver.find_element_by_id("c_rr14")
    restart_router_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "c_st28")))
    restart_confirm_button = driver.find_element_by_id("c_st28")
    restart_confirm_button.click()

driver.close()
