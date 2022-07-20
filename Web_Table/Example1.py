from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service()
driver=webdriver.Chrome(service=s)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)

#single column
single_col=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[3]/td[1]/a").text
print(single_col)

#Entire row
entire_row=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[3]").text
print(entire_row)

#Entire table
lis=driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")
print(len(lis))

for i in lis:
    print(i.text)