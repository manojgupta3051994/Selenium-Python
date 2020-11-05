from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'text/plain,application/pdf')
fp.set_preference('browser.download.manager.showWhenStarting',False)
fp.set_preference('browser.Download.dir','C:/Users/Manoj/source')
fp.set_preference('browser.download.folderList',2)
fp.set_preference('pdfjs.disabled',True)


driver = webdriver.Firefox(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\geckodriver.exe", firefox_profile=fp)

driver.get('http://demo.automationtesting.in/FileDownload.html')

driver.find_element_by_xpath('//*[@id="textbox"]').send_keys('Manoj Manoj Manoj')

driver.find_element_by_xpath('//*[@id="createTxt"]').click()

driver.find_element_by_id('link-to-download').click()