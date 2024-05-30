import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
#Implicite wait: global time out to the script: If anyelement not shown to page
# it took max time 5 sec in current scenario , if element is visible in 2 sec.
# it will imediat proceed without waiting for 5 sec
#implicit wait took time for executing every line of code

driver.implicitly_wait(10)

#Class name: .search-keyword
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

#in Case of Sleep: It will wait till 2 second though element will display in 1 second or not.
# Implicite wait is not work to Fetch list of elements from the page we required to give sleep time,
# aA it took time to Load each values of list,
time.sleep(2)
#Find elements plural should : //div[@class='products']/div[1]
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# count = len(results)
# assert count > 0
#Chaining Concept of Selenium

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#SUM Validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)          #48 +160 +

print(sum)
totalammount = int (driver.find_element(By.CSS_SELECTOR,".totAmt").text)

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

# Explicitly wait is , to wait for

time.sleep(4)









