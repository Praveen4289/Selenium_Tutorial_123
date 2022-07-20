from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service()
driver=webdriver.Chrome(service=s)
driver.get('http://www.google.com')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"q").send_keys("selenium")
list_suggestion=driver.find_elements(By.XPATH,"//ul[@class='erkvQe']/div/ul/li")
print(len(list_suggestion))
for i in list_suggestion:
    print(i.text)


for i in list_suggestion:
    if i.text=="selenium tutorial":
        i.click()