from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
driver.get("http://www.demo.guru99.com/v4/")
driver.find_element_by_name('uid').send_keys("mngr291573")
driver.find_element_by_name('password').send_keys("EzehUgu")
driver.find_element_by_name('btnLogin').click()
driver.implicitly_wait(10)
driver.close()
