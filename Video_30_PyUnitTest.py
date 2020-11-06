import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        self.driver.get('https://www.google.com/')
        print(self.driver.title)
        self.driver.close()
    
    def test_facebook(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        self.driver.get('https://www.facebook.com/')
        print(self.driver.title)
        self.driver.close()

if __name__ == "__main__" :
    unittest.main()
