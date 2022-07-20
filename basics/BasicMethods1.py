from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
actual_title=driver.title
print(actual_title)
actual_url=driver.current_url
print(actual_url)