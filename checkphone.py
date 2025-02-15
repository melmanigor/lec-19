import phone
import unittest
class TestPhone(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
    def test_not_3_prefix_digit(self):
        result=phone.check_phone("72-52-1234567")
        self.assertFalse(result,print("\nWrong phone number"))
    def test_missig_updach(self):
        result=phone.check_phone("97252-1234567")
        self.assertFalse(result,print("Missing upper dash"))
    def test_something(self):
        result=phone.check_phone("972-52-1234567")
        self.assertTrue(result,print("\nTest of good number"))
    def test_not_end_7digits(self):
        result=phone.check_phone("972-52-123456")
        self.assertFalse(result,print("\nNot finished with 7 digit"))
if __name__ == '__main__':    
    unittest.main()