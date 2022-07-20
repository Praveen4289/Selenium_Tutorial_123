from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0_')]").click()
act=ActionChains(driver)
ele=driver.find_element(By.NAME,"firstname")
ele.send_keys("Ram")
act.send_keys(Keys.TAB).send_keys("r").send_keys(Keys.TAB).\
    send_keys("abc@gmail.com").send_keys(Keys.TAB).send_keys("abc@gmail.com").\
    send_keys(Keys.TAB).send_keys("admin@123").perform()

