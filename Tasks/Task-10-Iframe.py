
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

s=Service()
driver=webdriver.Edge(service=s)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
driver.implicitly_wait(20)

page_text=driver.find_element(By.XPATH,"//*[@id='getwebsitebtn']").text
print("Default Page value:",page_text)


driver.switch_to.frame("iframeResult")
text1=driver.find_element(By.XPATH,"//h1[text()='The iframe element']").text
print("Frame 1 value:",text1)

f=driver.find_element(By.XPATH,"//iframe[@title='W3Schools Free Online Web Tutorials']")
driver.switch_to.frame(f)
text2=driver.find_element(By.XPATH,"//h1[text()='Learn to Code']").text
print("Frame 2 value:",text2)
driver.execute_script("window.scrollBy(0,550)")
driver.find_element(By.ID,"search2").send_keys("python")
driver.find_element(By.XPATH,"//i[@id='learntocode_searchicon']").click()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")



driver.switch_to.frame("iframeResult")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='W3Schools Free Online Web Tutorials']"))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='howto_iframe']"))
text3=driver.find_element(By.XPATH,"//div[text()='Caption Text']").text
print("Frame 3 value:",text3)


driver.switch_to.default_content()
page_text1=driver.find_element(By.XPATH,"//button[@id='runbtn']").text
print("Default Page value:",page_text1)

driver.close()