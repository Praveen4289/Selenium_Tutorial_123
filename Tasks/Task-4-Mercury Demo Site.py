import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s=Service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get('http://demo.guru99.com/test/newtours')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Register here').click()
driver.find_element(By.NAME,'firstName').send_keys('Praveen Kumar')
driver.find_element(By.NAME,'lastName').send_keys('Natarajan')
driver.find_element(By.NAME,'phone').send_keys('7904908951')
driver.find_element(By.ID,'userName').send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.NAME,'address1').send_keys('NO.94,Madam street,Pilliyarpalliyam')
driver.find_element(By.NAME,'city').send_keys('Kachipuram')
driver.find_element(By.NAME,'state').send_keys('TamilNadu')
driver.find_element(By.NAME,'postalCode').send_keys('631501')
driver.find_element(By.NAME,'email').send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.NAME,'password').send_keys('Qwerty@123')
driver.find_element(By.NAME,'confirmPassword').send_keys('Qwerty@123')
driver.find_element(By.NAME,'country').send_keys('INDIA')
time.sleep(5)
driver.find_element(By.NAME,'submit').click()
driver.get('https://demo.guru99.com/test/newtours/login.php')
time.sleep(2)
driver.find_element(By.NAME,'userName').send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.NAME,'password').send_keys('Qwerty@123')
driver.find_element(By.NAME,'submit').click()
time.sleep(10)
driver.close()


