from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
element = driver.find_element_by_id('select-demo')
drop = Select(element)

drop.select_by_visible_text('Sunday')

drop.select_by_index(5)

print(len(drop.options))

for options in drop.options:
    print(options.text)


