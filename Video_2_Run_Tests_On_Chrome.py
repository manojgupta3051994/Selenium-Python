from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
driver.get("https://www.msn.com/en-in")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
