import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s = Service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get('https://www.rediff.com/')
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/p/a[2]").click()
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[3]/td[3]/input").send_keys("Praveenkumar Natarajan")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[7]/td[3]/input[1]").send_keys("praveennatarajan007")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[7]/td[3]/input[2]").click()
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[9]/td[3]/input").send_keys("Qwerty@123")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[11]/td[3]/input").send_keys("Qwerty@123")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[14]/td/div/table/tbody/tr[1]/td[3]/input").send_keys("praveennatarajan007@gmail.com")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[20]/td/div/table/tbody/tr/td[3]/div[3]/input").send_keys("7904908951")
time.sleep(10)
driver.close()
