import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s = Service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get('https://www.rediff.com/')
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@title='Create Rediffmail Account']").click()
driver.find_element(By.XPATH, "//input[starts-with(@name,'name')]").send_keys('Praveenkumar Natarajan')
driver.find_element(By.XPATH, "//input[starts-with(@name,'login')]").send_keys('praveennatarajan007')
driver.find_element(By.XPATH, "//input[@type='button'][contains(@name,'btnchkavail')]").click()
driver.find_element(By.XPATH, "//input[starts-with(@name,'passw')]").send_keys('Qwerty@123')
driver.find_element(By.XPATH, "//input[starts-with(@name,'confirm_pass')]").send_keys('Qwerty@123')
driver.find_element(By.XPATH, "//input[starts-with(@name,'altemail')]").send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.XPATH,"//div[@onclick='javascript: openDiv(event);']").click()
contry_list=driver.find_elements(By.XPATH,"//div[@id='country_id']//ul/li")
for i in contry_list:
    if i.text=="India (+91)":
        i.click()
        break
driver.find_element(By.XPATH, "//input[starts-with(@name,'mobno')]").send_keys('7904908951')
driver.find_element(By.XPATH, "//option[text()='04']").click()
driver.find_element(By.XPATH, "//option[text()='FEB']").click()
driver.find_element(By.XPATH, "//option[text()='1997']").click()
driver.find_element(By.XPATH, "//input[@type='radio'][@value='m']").click()
driver.find_element(By.XPATH, "//option[@label='India']").click()
driver.find_element(By.XPATH, "//option[@label='Vellore']").click()
time.sleep(10)
driver.close()
