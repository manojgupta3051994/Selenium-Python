from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://testautomationpractice.blogspot.com/')

driver.maximize_window()

driver.switch_to_frame(0)

elem = driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]').send_keys('C:/Users/Manoj/Pictures/PhotoDirector/8.0/Manoj')
