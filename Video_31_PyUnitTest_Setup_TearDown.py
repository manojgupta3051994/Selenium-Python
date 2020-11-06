import unittest

def setUpModule():
    print("SetupModule")

def tearDownModule():
    print("TearDownModule")

class Application(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class level")

    def setUp(self):
        print("This is Setup")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search test")

    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is search test")

    def tearDown(self):
        print("This is Tear Down")

    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class level")

if __name__ == '__main__':
    unittest.main()