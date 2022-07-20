import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.find_element(By.NAME,"proceed").click()
alt=driver.switch_to.alert
time.sleep(5)
print(alt.text)
alt.accept()