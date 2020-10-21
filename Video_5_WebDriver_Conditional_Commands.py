from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
email = driver.find_element_by_xpath("//*[@id='email']")
password = driver.find_element_by_xpath("//*[@id='pass']")
print(email.is_displayed())
print(email.is_enabled())
username_ele = email.send_keys("asd@asd.com")
password_ele = password.send_keys("asdasdadasd")
login = driver.find_element_by_xpath("//*[@id='u_0_b']").click()
driver.close()