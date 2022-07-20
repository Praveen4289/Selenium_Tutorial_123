from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"email").send_keys("RamKumar")

typed_text=driver.find_element(By.ID,"email").get_attribute("value")
print(typed_text)

attr_value=driver.find_element(By.ID,"email").get_attribute("aria-label")
print(attr_value)

st=driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").value_of_css_property("height")
print(st)
