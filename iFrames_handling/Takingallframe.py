from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)

frame_list=driver.find_elements(By.TAG_NAME,"iframe")
print(len(frame_list))

for i in frame_list:
    print(i.get_attribute("id"),"--->", i.get_attribute("name"))