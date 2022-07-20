import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s=Service()
driver=webdriver.Edge(service=s)
driver.get("http://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("9566534306")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("Flipkart@1997")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("smartpho")
time.sleep(5)
list_1=driver.find_elements(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/ul/li")
time.sleep(5)
print(len(list_1))
time.sleep(15)

for i in list_1:
    print(i.text)
    if i.text == "smartphone 10000":
        i.click()
        break

print("=========================================================================")
time.sleep(10)
driver.execute_script("window.scrollBy(0,1400)")

driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[6]/div/div/div/a").click()

print('Before switching parent to child:',driver.title)

parent_window=driver.current_window_handle
child_win=driver.window_handles
for i in range(len(child_win)):
    if child_win[i]!=parent_window:
        driver.switch_to.window(child_win[i])
        print('After switching parent to child',driver.title)
        child_text=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span").text
        print('Name of the product:',child_text)
        driver.close()
        break

driver.switch_to.window(parent_window)

print('After switching child to parent:',driver.title)



