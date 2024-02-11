import unittest
from vowel_numbers import count_vowels

class TestVowelNumbers(unittest.TestCase):
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_mixed_input(self):
        self.assertEqual(count_vowels("hello world"), 3)

    def test_case_sensitivity(self):
        self.assertEqual(count_vowels("AEioU"), 5)

    def test_empty_input(self):
        self.assertEqual(count_vowels(""), 0)

if __name__ == "__main__":
    unittest.main()