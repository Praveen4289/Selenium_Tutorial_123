# Reqirement: open amazon.in and sign-in and search product and pick from auto suggestion and scroll down to 5th product and place add to cart.

#Imported Files
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as edge_service

# Required Web Elements
url="http://www.amazon.in"
signintab_Xpath="/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]"
signinButton_xpath="/html/body/div[1]/header/div/div[3]/div[3]/div[2]/div/div[1]/div/a"
userid_xpath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]"
continue_xpath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input"
pass_xpath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/input"
submit_xpath="/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input"
username_xpath="/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span"
searchinput_xpath="/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input"
suggestion_list_xpath="/html/body/div[1]/header/div/div[2]/div/div[2]/div"
fifth_product_xpath="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[7]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a"
product_name_xpath="/html/body/div[4]/div[2]/div[3]/div[11]/div[3]/div/h1/span"
add_cart_xpath="/html/body/div[4]/div[2]/div[3]/div[8]/div[7]/div/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[32]/div[1]/span/span/span/input"

#Browser Driver
driver=webdriver.Edge(service=edge_service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe"))
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

#Home page Navigate to Sign in tab
signintab=driver.find_element(By.XPATH,signintab_Xpath)
act=ActionChains(driver)
act.move_to_element(signintab).perform()
driver.find_element(By.XPATH,signinButton_xpath).click()


#Sign in tab
driver.find_element(By.XPATH,userid_xpath).send_keys("7904908951")
driver.find_element(By.XPATH,continue_xpath).click()
driver.find_element(By.XPATH,pass_xpath).send_keys("Amazon@1997")
driver.find_element(By.XPATH,submit_xpath).click()

#validating sign_in  by printing user name
usr_name=driver.find_element(By.XPATH,username_xpath).text
print(usr_name)
if usr_name=="Hello, Praveen":
    print("##############Sign_in successful################")
else:
    print("##############sign in failed################")

#performing search and auto suggestion

driver.find_element(By.XPATH,searchinput_xpath).send_keys("Iphone")
suggestion_list=driver.find_elements(By.XPATH,suggestion_list_xpath)
print("Number of Auto Suggestion :",len(suggestion_list))

for i in suggestion_list:
    if i.text=="iphone 13":
        i.click()
        break


#Scroll down to 5th product and click
driver.execute_script("window.scrollBy(0,1350)")
driver.find_element(By.XPATH,fifth_product_xpath).click()

#switching to child window and perfoming add to cart and validateing
print("Before switching child to Parent window --> Title:",driver.title)
parent_window=driver.current_window_handle
child_win=driver.window_handles
for i in range(len(child_win)):
    if child_win[i]!=parent_window:
        driver.switch_to.window(child_win[i])
        print('After switching parent to Child window --> Title:',driver.title)
        child_text=driver.find_element(By.XPATH,product_name_xpath).text
        print('Name of the product is:',child_text)
        driver.find_element(By.XPATH,add_cart_xpath).click()
        print("###############Product Added To Cart Successfuly################")
        break

driver.switch_to.window(parent_window)
print("After switching child to Parent window --> Title:",driver.title)

driver.quit()
