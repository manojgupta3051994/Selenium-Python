from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get("https://www.makemytrip.com/flights/")

links = driver.find_elements(By.TAG_NAME,'a')

print (links)

for l in links:
    print(l.text)

driver.find_element(By.LINK_TEXT,'About Us').click()

driver.find_element(By.PARTIAL_LINK_TEXT,'About').click()