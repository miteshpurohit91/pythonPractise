import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver service: It plays a key role to invoke chrome browser
#chrome driver service
#service_obj = Service("D:\Python_Practise\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#Edge driver service
#service_obj = Service("D:\Python_Practise\msedgedriver.exe")
#Firefoxdriver -> geckodriver

#Pass above object value at service attribute
driver = webdriver.Edge(service=service_obj)

#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)























time.sleep(2)