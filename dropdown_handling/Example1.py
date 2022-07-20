import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_2_')]").click()
month_drop=driver.find_element(By.ID,"month")
sel=Select(month_drop)
sel.select_by_visible_text("Oct")
time.sleep(5)
sel.select_by_value("5")
time.sleep(5)
sel.select_by_index(11)