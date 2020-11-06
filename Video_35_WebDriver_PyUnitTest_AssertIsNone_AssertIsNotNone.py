import unittest
from selenium import webdriver

class App(unittest.TestCase):

    def test_search(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        driver1 = None
        self.assertIsNone(driver1)
        self.assertIsNotNone(driver)

if __name__ == '__main__':
    unittest.main()
        