from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print (driver.current_window_handle)

handles = driver.window_handles

for h in handles:
    driver.switch_to_window(h)
    print(driver.title)
    if driver.title == "SeleniumHQ Browser Automation":
        driver.close