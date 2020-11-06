import unittest

class Test(unittest.TestCase):
    def test(self):
        list = ["Manoj","Ajay","Kailash","Sujeet"]
        self.assertIn("Manoj",list)
        self.assertNotIn("Mano",list)

if __name__ == '__main__':
    unittest.main()