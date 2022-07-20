from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path='E:\\Software Testing\\5.Tools\\chromedriver_win32\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("http://www.youtube.com")
driver.maximize_window()
Title=driver.title
print(Title)
Url=driver.current_url
print(Url)
driver.close()