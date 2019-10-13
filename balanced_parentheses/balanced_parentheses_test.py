import sys
import unittest
from balanced_parentheses import is_string_balanced

class TestBueller(unittest.TestCase):

    def setUp(self):
        pass

    def test_sinlge_balanced(self):
        string = "(This string is balanced)"
        self.assertTrue(is_string_balanced(string))

    def test_multiple_balanced_1(self):
        string = "(This (string is) balanced)"
        self.assertTrue(is_string_balanced(string))

    def test_multiple_balanced_2(self):
        string = "(This) string is (balanced)"
        self.assertTrue(is_string_balanced(string))

    def test_multiple_balanced_3(self):
        string = "(This) (string is (balanced))"
        self.assertTrue(is_string_balanced(string))

    def test_wrong_order(self):
        string = ")This string is not balanced("
        self.assertFalse(is_string_balanced(string))

    def test_only_open(self):
        string = "(This (string is not balanced("
        self.assertFalse(is_string_balanced(string))

    def test_only_close(self):
        string = ")This )string is not balanced)"
        self.assertFalse(is_string_balanced(string))

    def test_unbalanced_1(self):
        string = "(This) string is not balanced)"
        self.assertFalse(is_string_balanced(string))

    def test_unbalanced_2(self):
        string = "(This) string is not balanced)("
        self.assertFalse(is_string_balanced(string))

    def test_unbalanced_3(self):
        string = "((This string is not balanced)("
        self.assertFalse(is_string_balanced(string))

if __name__ == '__main__':
    unittest.main()