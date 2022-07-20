from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
src=driver.find_element(By.ID,"draggable")
des=driver.find_element(By.ID,"droppable")
act=ActionChains(driver)
act.drag_and_drop(src,des).perform()
