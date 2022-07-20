'''
1) Mouse Hover --> ActionChains --> move_to_element
2) Right click --> ActionChanis --> context_click
3) Double click --> ActionChanis --> double_click
4) Drag and Drop --> ActionChanis --> drag_and_drop
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(30)
Jobs_ele=driver.find_element(By.XPATH,"//div[text()='Jobs']")
act=ActionChains(driver)
act.move_to_element(Jobs_ele).perform()
driver.find_element(By.XPATH,"//a[@title='IT jobs']").click()