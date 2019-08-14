import unittest
from palindrome_check import check_palindrome


class TestPalindromeCheck(unittest.TestCase):
    # ------------ TEST PALINDROME CASES-------------------------
    def test_palindrome_case_1(self):
        check_string = "abccba"
        self.assertTrue(check_palindrome(check_string),
                        "String {0} must be palindrome".format(check_string))

    def test_palindrome_case_2(self):
        check_string = "a"
        self.assertTrue(check_palindrome(check_string),
                        "String {0} must be palindrome".format(check_string))

    def test_palindrome_case_3(self):
        check_string = "aa"
        self.assertTrue(check_palindrome(check_string),
                        "String {0} must be palindrome".format(check_string))

    def test_palindrome_case_4(self):
        check_string = ""
        self.assertTrue(check_palindrome(check_string),
                        "String {0} must be palindrome".format(check_string))

    def test_palindrome_case_5(self):
        check_string = "abcdcba"
        self.assertTrue(check_palindrome(check_string),
                        "String {0} must be palindrome".format(check_string))
        
    # --------------- TEST NOT PALINDROME CASES -------------------------
    def test_not_palindrome_case_1(self):
        check_string = "abcde"
        self.assertFalse(check_palindrome(check_string),
                        "String {0} mustn't be palindrome".format(check_string))

    def test_not_palindrome_case_2(self):
        check_string = "abccbb"
        self.assertFalse(check_palindrome(check_string),
                        "String {0} mustn't be palindrome".format(check_string))

    def test_not_palindrome_case_3(self):
        check_string = "abcdba"
        self.assertFalse(check_palindrome(check_string),
                        "String {0} mustn't be palindrome".format(check_string))

    def test_not_palindrome_case_4(self):
        check_string = "aab"
        self.assertFalse(check_palindrome(check_string),
                        "String {0} mustn't be palindrome".format(check_string))


if __name__ == '__main__':
    unittest.main()
