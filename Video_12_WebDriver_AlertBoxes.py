from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://testautomationpractice.blogspot.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

driver.switch_to_alert().accept()

driver.switch_to_alert().dismiss()