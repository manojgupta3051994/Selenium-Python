from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html')

driver.switch_to_frame('packageListFrame')
driver.find_element_by_xpath('/html/body/div[2]/ul/li[5]/a').click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame('packageFrame')
driver.find_element_by_xpath('/html/body/div/ul/li[11]/a/span').click()
time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame('classFrame')
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()