import Video_26_WebDriver_XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://www.demo.guru99.com/v4/')

driver.maximize_window()

path = "C:/Users/Manoj/Desktop/Python - Selenium Practice/Drivers/Test.xlsx"

rows = Video_26_WebDriver_XLUtils.getRowCount(path,'Sheet1')


for r in range(2,rows+1):
    
    username = Video_26_WebDriver_XLUtils.readData(path,'Sheet1',r,1)
    password = Video_26_WebDriver_XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_name('uid').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_name('btnLogin').click()

    if driver.title == "Guru99 Bank Manager HomePage":
        print("test is passed")
        Video_26_WebDriver_XLUtils.writeData(path,'Sheet1',r,3,'Test is Passed')
        driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[15]/a').click()
        driver.switch_to_alert().accept()
    else:
        print("test is failed")
        Video_26_WebDriver_XLUtils.writeData(path,'Sheet1',r,3,'Test is Failed')
        driver.switch_to_alert().accept()
    


    

    

    
