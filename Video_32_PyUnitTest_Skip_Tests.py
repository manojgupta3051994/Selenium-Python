import unittest

class AppTest(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping the test")
    def test_advancedsearch(self):
        print("This is advanced search test")

    @unittest.skipIf(1==1,"Numbers are not equal")
    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is search test")


if __name__ == '__main__':
    unittest.main()