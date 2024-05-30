import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

name = "Mitesh"
surname = "Purohit"
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
#alert Methods, .text for read text from popup, .accept to give positive responce to popup, .dismis to decline popup

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
time.sleep(4)
assert name in alerttext
alert.accept()


time.sleep(4)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys(surname)
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
alert2 = driver.switch_to.alert
alerttext2 = alert2.text
print(alerttext2)
time.sleep(4)
assert surname in alerttext2
alert.dismiss()

time.sleep(4)