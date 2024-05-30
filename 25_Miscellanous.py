import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

#Headless Mode: Browser is run without open UI
chrome_options = webdriver.ChromeOptions() #We use chromeoption class of webdriver
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("headless") #we have to provide an argument in chrom option

#service_object = Service ("D:\\Python_Practise\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000);")
driver.get_screenshot_as_file("screen.jpg")
time.sleep(4)