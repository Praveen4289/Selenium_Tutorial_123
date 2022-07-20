from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
driver.find_element(By.NAME,"firstname").send_keys("RAM")
parent_window=driver.current_window_handle
driver.find_element(By.ID,"cookie-use-link").click()
child_win=driver.window_handles
for i in range(len(child_win)):
    if child_win[i]!=parent_window:
        driver.switch_to.window(child_win[i])
        print(driver.title)
        child_text=driver.find_element(By.XPATH,"//h2[contains(text(),'Cookies')]").text
        print(child_text)
        driver.close()
        break

driver.switch_to.window(parent_window)
driver.find_element(By.NAME,"lastname").send_keys("Kumar")