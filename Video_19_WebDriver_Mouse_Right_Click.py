from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")


driver.get('https://swisnl.github.io/jQuery-contextMenu/demo/input.html')

action = ActionChains(driver)

elem = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
text = driver.find_element_by_name('context-menu-input-name')
action.context_click(elem).move_to_element(text).click().send_keys('Manoj').perform()