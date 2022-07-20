import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s=Service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get('http://demo.guru99.com/test/newtours')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Register here').click()
driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys('Praveen Kumar')
driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys('Nadarajan')
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys('7904908951')
driver.find_element(By.XPATH,"//input[@id='userName']").send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.XPATH,"//input[@name='address1']").send_keys('No-94,Madam Street,PIlliyarpalliyam')
driver.find_element(By.XPATH,"//input[@name='city']").send_keys('Kanchipuram')
driver.find_element(By.XPATH,"//input[@name='state']").send_keys('Tamil Nadu')
driver.find_element(By.XPATH,"//input[@name='postalCode']").send_keys('631501')
driver.find_element(By.XPATH,"//select[@name='country']").send_keys('INDIA')
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Qwerty@123")
driver.find_element(By.XPATH,"//input[@name='confirmPassword']").send_keys('Qwerty@123')
driver.find_element(By.XPATH,"//input[@name='submit']").click()
driver.get("https://demo.guru99.com/test/newtours/login.php")
driver.find_element(By.XPATH,"//input[@name='userName']").send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('Qwerty@123')
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(7)
driver.close()