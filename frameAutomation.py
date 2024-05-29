import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(4)

# driver.switch_to.frame("mce_0_ifr")
# time.sleep(4)
# driver.find_element(By.XPATH,"//div[@aria-label='Close']").click()
# driver.find_element(By.ID,"tinymce").clear()
# driver.find_element(By.ID,"tinymce").send_keys("I am automating frame")
#driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text)