from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
#Single attribute

#driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Arul")
driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']").send_keys("Praveen")
driver.find_element(By.XPATH,"//input[@data-testid='royal_pass']").send_keys("Karthik")
#driver.find_element(By.XPATH,"//button[@data-testid='royal_login_button']").click()

#text function

forgot_text1=driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").text
print("Text () = ",forgot_text1)

#contains()--->text()

forgot_text2=driver.find_element(By.XPATH,"//a[contains(text(),'d?')]").text
print("Contains()--> Text() =",forgot_text2)

#starts-with()---> text()

forgot_text3=driver.find_element(By.XPATH,"//a[starts-with(text(),'Fo')]").text
print("starts-with()---> Text()",forgot_text3)

#driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()

#contains()--> attribute

#driver.find_element(By.XPATH,"//a[contains(@id,'_0_2_')]").click()

#starts-with()---> attribute

driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_2_')]").click()

#Multiple attribute
driver.find_element(By.XPATH,"//input[@class='_8esa'][@value=2]").click()

