from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
driver.find_element(By.NAME,"firstname").send_keys("Admin")
