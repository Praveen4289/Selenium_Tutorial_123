from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)
rele=driver.find_element(By.XPATH,"//span[text()='right click me']")
act=ActionChains(driver)
act.context_click(rele).perform()