from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

s=Service(executable_path="E:/Software Testing/5.Tools/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/p/a[2]").click()
driver.find_element(By.XPATH,"//*[@id='tblcrtac']/tbody/tr[7]/td[3]/input[1]").send_keys('praveennatarajan007')
driver.find_element(By.XPATH,"//*[@id='tblcrtac']/tbody/tr[7]/td[3]/input[2]").click()
driver.find_element(By.XPATH,"//*[@id='tblcrtac']/tbody/tr[9]/td[3]/input").send_keys('Qwerty@123')
driver.find_element(By.XPATH,"//*[@id='tblcrtac']/tbody/tr[11]/td[3]/input").send_keys('Qwerty@123')
driver.find_element(By.XPATH,"//*[@id='div_altemail']/table/tbody/tr[1]/td[3]/input").send_keys('praveennatarajan007@gmail.com')
driver.find_element(By.XPATH,"//*[@id='mobno']").send_keys('7904908951')
driver.find_element(By.XPATH,"//*[@id='tblcrtac']/tbody/tr[24]/td[3]/input[1]").click()
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[3]/td[3]/input").send_keys("Praveenkumar Natarajan")
month=driver.find_element(By.XPATH,"//select[starts-with(@name,'DOB_Month')]")
sel=Select(month)
sel.select_by_visible_text("DEC")
country_code=driver.find_elements(By.XPATH,"//div[@id='country_id']/ul/li")
print(len(country_code))

for i in country_code:
    print(i.text)

