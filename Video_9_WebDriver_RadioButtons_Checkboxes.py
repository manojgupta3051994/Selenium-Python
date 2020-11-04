from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")


driver.get("http://www.demo.guru99.com/v4/")
driver.find_element_by_name('uid').send_keys("mngr291573")
driver.find_element_by_name('password').send_keys("EzehUgu")
driver.find_element_by_name('btnLogin').click()

driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()


stat = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]').is_selected()
print(stat)

driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]').click()

stat = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]').is_selected()
print(stat)
