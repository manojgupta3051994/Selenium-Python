from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('https://www.w3schools.com/html/html_tables.asp')

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
print(rows)

cols = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))
print(cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr["+str(r)+"]/td["+str(c)+"]').text
        print(value, end= "     ")
    print()


    