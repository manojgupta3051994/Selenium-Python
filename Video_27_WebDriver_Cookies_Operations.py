from selenium import  webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')

driver.get('https://www.amazon.in/ref=nav_logo')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

new = {'name':'Manoj','value':'123456789'}

driver.add_cookie(new)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies
print(len(cookies))