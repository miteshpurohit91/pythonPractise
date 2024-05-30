import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Top Deals']").click()


windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])

#click on column Header
#collectio all Vegie names --> Vegielist
#Sort this Vegielist --> Sorted Vegilist
#Vegielist == newSortedlist

time.sleep(4)