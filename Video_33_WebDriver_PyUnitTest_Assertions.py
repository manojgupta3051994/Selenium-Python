import unittest
from selenium import webdriver

class App(unittest.TestCase):

    def test_search(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        self.driver.get('https://www.google.com/')
        title = self.driver.title
        self.assertEqual("Google",title,'Failed')
        self.driver.close()

    def test_searches(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        self.driver.get('https://www.Facebook.com/')
        title = self.driver.title
        self.assertNotEqual("Google",title,'Failed Facebook')

if __name__ == '__main__':
    unittest.main()