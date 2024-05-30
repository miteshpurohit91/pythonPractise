import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()

# by using windows_handles Property we can open window
windowsopend = driver.window_handles
driver.switch_to.window(windowsopend[1])
print(driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
driver.close()
driver.switch_to.window(windowsopend[0])
assert "Opening a new window" == driver.find_element(By.XPATH, "//h3[normalize-space()='Opening a new window']").text
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am automating frame")