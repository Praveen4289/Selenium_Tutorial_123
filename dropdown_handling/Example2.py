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

year_dd=driver.find_element(By.ID,"year")

sel=Select(year_dd)
dd_list=sel.options
print(len(dd_list))

for i in dd_list:
    print(i.text)

