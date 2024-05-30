import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(4)