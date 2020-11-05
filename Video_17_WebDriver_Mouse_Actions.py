from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")

driver.get('http://automationpractice.com/index.php')

actions = ActionChains(driver)

interactions = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a')
dad = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/ul/li[2]/a')


actions.move_to_element(interactions).move_to_element(dad).click().perform()