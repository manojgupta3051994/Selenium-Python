from selenium import webdriver
from selenium.webdriver.chrome.options import Options

co = Options()
co.add_experimental_option('prefs',{'download.default_directory':'C:/Users/Manoj/source'})

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe",chrome_options=co)

driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.find_element_by_xpath('//*[@id="textbox"]').send_keys('Manoj Manoj Manoj')

driver.find_element_by_xpath('//*[@id="createTxt"]').click()

driver.find_element_by_id('link-to-download').click()