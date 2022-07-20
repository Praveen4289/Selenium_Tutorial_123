from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.justdial.com")
driver.maximize_window()
driver.implicitly_wait(30)
#driver.save_screenshot("C:\\Users\\pc\\Desktop\\Demo\\Frist_Screen_shot.png")
driver.get_screenshot_as_file("C:\\Users\\pc\\Desktop\\Demo\\Second_Screen_shot.png")