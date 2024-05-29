import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(4)


# We are using Actionchains class to execute actions on browser
action = ActionChains(driver)

# action.click_and_hold() : click and long press
#action.double_click(driver.find_element(By.))
#action.drag_and_drop() : give source and destination element id

action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #If we use action method then need to close it with .perform
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()  #Right click on Element
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()  #Right click on Element

time.sleep(10)


