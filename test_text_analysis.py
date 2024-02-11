import unittest
from vowel_numbers import count_vowels
from word_numbers import count_words

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

class TestWordNumbers(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_multiple_words(self):
        self.assertEqual(count_words("hello there world"), 3)
    
    def test_multiple_spaces(self):
        self.assertEqual(count_words("hello    world"), 2)
    
    def test_empty_input(self):
        self.assertEqual(count_words(""), 0)
    
    def test_insert_punctuation(self):
        self.assertEqual(count_words("Hello, world! "), 2)

if __name__ == "__main__":
    unittest.main()