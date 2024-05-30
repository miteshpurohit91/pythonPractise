import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#ID, XPATH, Class name, linked text locators provide to identified element on the page
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()

#To create Xpath for any element: //tagname[@attribute= 'value']
#To Create custom CSS selector: tagname[attribute=value"], #id, .classname

#Static Dropdown --> Will use Select class for it, We can find element with help by
#1. using index
#2. using visible text
#3. using value

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
#dropdown.select_by_value()


#driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello again")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(5)