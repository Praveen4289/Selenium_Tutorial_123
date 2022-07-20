from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
#id
driver.find_element(By.ID,"email").send_keys("Admin")
#name 
driver.find_element(By.NAME,"pass").send_keys("admin123")
#classname
str1=driver.find_element(By.CLASS_NAME,"_8eso").text
print(str1)

#link text
#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()

#partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"word").click()