import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_object = Service("D:\\Python_Practise\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)

#CSS selector syntax as, tagname[attribute='value'] tagname
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a ")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
assert (driver.find_element(By.ID,"autosuggest").get_attribute("value")) == "BAsIndia                                                                                                                                                                                                                                                                          "
time.sleep(5)

