from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')

driver.maximize_window()

#   Scroll Down by Pixel Range
driver.execute_script("window.scrollBy(0,1000)"," ")

#   Scroll Down to given element

elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();",elem)

#   Scroll down till bottom of page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


