from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
time.sleep(2)
driver.get("https://pavanonlinetrainings.com/")
print(driver.title)
driver.back()
time.sleep(2)
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(3)
driver.close()