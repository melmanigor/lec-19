import unittest
import productname

class TestCheckname(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    def test_not2letters(self):
         result=productname.check_product_name("a")
         self.assertFalse(result,print("\nThe name should be 2 letters"))
    def test_correctname(self):
        result=productname.check_product_name("Juice")
        self.assertTrue(result,print("\nCorrect product name "))
    def test_morethan50letters(self):
        result=productname.check_product_name("g"*49)
        self.assertFalse(result,print("\nMore than 50 Letters"))
if __name__ == '__main__':    
    unittest.main()
    
    