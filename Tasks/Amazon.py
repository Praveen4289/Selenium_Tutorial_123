import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

edge_service=Service()
driver=webdriver.Edge(service=edge_service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.amazon.in/")
search=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search.click()
search.send_keys("smartphones")
time.sleep(5)
search_list=driver.find_elements(By.XPATH,"/html/body/div[1]/header/div/div[2]/div/div[2]/div")
time.sleep(5)
print(len(search_list))
time.sleep(5)
for i in search_list:
    print(i.text)
    if i.text == "smartphones under 10000":
        i.click()
        break

time.sleep(5)

driver.execute_script("window.scrollBy(0,1350)")

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a").click()

parent_window=driver.current_window_handle
child_win=driver.window_handles
for i in range(len(child_win)):
    if child_win[i]!=parent_window:
        driver.switch_to.window(child_win[i])
        print('After switching parent to child',driver.title)
        child_text=driver.find_element(By.XPATH,"//span[@id='productTitle']").text
        print('Name of the product:',child_text)
        driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']").click()
        login=driver.find_element(By.XPATH,"//input[@id='ap_email']")
        login.clear()
        login.send_keys("9566534306")
        driver.find_element(By.XPATH,"//input[@id='continue']").click()
        passw=driver.find_element(By.XPATH,"//input[@id='ap_password']")
        passw.clear()
        passw.send_keys("Amazon@1997")
        driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
        driver.find_element(By.XPATH,"//a[@id='auth-get-new-otp-link']").click()
        driver.find_element(By.XPATH,"//input[@value='4PDki+Hc0EWYxO+pwojOGkXETM6JM0GBjxJY/lNaIYw=, SMS']").click()
        driver.find_element(By.XPATH,"//input[@id='auth-send-code']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/span/span/input").click()




