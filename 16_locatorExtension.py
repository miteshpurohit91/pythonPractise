import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()

#Creating X-Path from Parent to child Traversing

#driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("demo@gmail.com")

#Creating CSS from Parent to child Traversing by making a space between elements

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@1234")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Create X-path based on text
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(5)