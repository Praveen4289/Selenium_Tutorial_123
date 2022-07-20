from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"html/body/div/div[2]/div/div/div/div/div[2]/div/div/form/div/div/input").send_keys("Admin")
driver.find_element(By.XPATH,"html/body/div/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div/input").send_keys("admin123")
