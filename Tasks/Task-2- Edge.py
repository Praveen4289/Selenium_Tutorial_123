from selenium import webdriver
from selenium.webdriver.edge.service import Service

s=Service(executable_path="E:\\Software Testing\\5.Tools\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get('http://www.youtube.com')
driver.maximize_window()
Title=driver.title
print(Title)
Url=driver.current_url
print(Url)
driver.close()

