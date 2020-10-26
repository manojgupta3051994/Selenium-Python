from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
driver.get("http://www.demo.guru99.com/v4/")
driver.find_element_by_name('uid').send_keys("mngr291573")
driver.find_element_by_name('password').send_keys("EzehUgu")
driver.find_element_by_name('btnLogin').click()
wait = WebDriverWait(driver,5)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='navbar-brand-centered']")))
element.click()
time.sleep(2)
driver.close()


