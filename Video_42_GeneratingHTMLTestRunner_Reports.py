from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHrmTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_HomePageTitle(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.assertEqual("OrangeHRM",self.driver.title,"Webpage Title is not same")

    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        self.assertEqual("OrangeHRM",self.driver.title,"Webpage Title is not same")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='C:\\Users\Manoj\Desktop\Python - Selenium Practice\Reports'))