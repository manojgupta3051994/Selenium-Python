from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source_elem = driver.find_element_by_xpath('//*[@id="box6"]')
target_elem = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)

actions.drag_and_drop(source_elem,target_elem).perform()