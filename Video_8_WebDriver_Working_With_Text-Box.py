from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get("http://www.demo.guru99.com/v4/")


# Number of Textboxes, Feeding in Data
name = driver.find_element_by_name('uid').send_keys("mngr291573") , driver.find_element(By.NAME,'password').send_keys("EzehUgu")
print(len(name))


# Checking status of textboxes
enabled = driver.find_element(By.NAME,'uid').is_enabled()
print(enabled)