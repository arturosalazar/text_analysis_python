import unittest
from vowel_numbers import count_vowels
from word_numbers import count_words
from character_numbers import count_characters

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

class TestCharacterNumbers(unittest.TestCase):
    def test_letters_only(self):
        self.assertEqual(count_characters("sometext"), 8)

    def test_with_spaces(self):
        self.assertEqual(count_characters("some text"), 9)

    def test_with_punctuation(self):
        self.assertEqual(count_characters("Hello, world!"), 13)

    def test_with_special_characters(self):
        self.assertEqual(count_characters("#$@%^&*()!"), 10)

    def test_numbers(self):
        self.assertEqual(count_characters("534211"), 6)

    def test_empty_input(self):
        self.assertEqual(count_characters(""), 0)
    
    def test_single_letter(self):
        self.assertEqual(count_characters("a"), 1)

    def test_spaces_input(self):
        self.assertEqual(count_characters("    "), 4)
        
if __name__ == "__main__":
    unittest.main()