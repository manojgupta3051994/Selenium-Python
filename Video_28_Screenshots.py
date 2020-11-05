from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('https://www.amazon.in/ref=nav_logo')

driver.save_screenshot('C:/Users/Manoj/Desktop/Python - Selenium Practice/Drivers/new.jpg')

driver.get_screenshot_as_file('C:/Users/Manoj/Desktop/Python - Selenium Practice/Drivers/new.png')