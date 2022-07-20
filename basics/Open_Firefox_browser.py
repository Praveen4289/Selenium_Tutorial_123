from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s=Service(executable_path="D:\\SeleniumDrivers\\gecko31\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("http://www.rediff.com")