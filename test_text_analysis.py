import unittest
from vowel_numbers import count_vowels
from word_numbers import count_words
from character_numbers import count_characters
from spell_checker import is_valid_word_nltk, format_word_list, check_word_list

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

class TestIsValidWordNltk(unittest.TestCase):
    def test_valid_word(self):
        self.assertEqual(is_valid_word_nltk("example"), True)
    
    def test_valid_word_upper_case(self):
        self.assertEqual(is_valid_word_nltk("EXAMPLE"), True)
    
    def test_invalid_word(self):
        self.assertEqual(is_valid_word_nltk("wroask"), False)

class TestFormatWordList(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(format_word_list("python"), ["python"])

    def test_multiple_word(self):
        self.assertEqual(format_word_list("python is cool"), ["python", "is", "cool"])

    def test_string_with_punctuation(self):
        self.assertEqual(format_word_list("Python, is - the ? coolest !"), ["Python", "is", "the", "coolest"])

    def test_string_with_numbers(self):
        self.assertEqual(format_word_list("Python 3 is better than Python 2"), ["Python", "is", "better", "than", "Python"])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(format_word_list("Hello    there  ,World!"), ["Hello", "there", "World"])

    def test_gibberish_string(self):
        self.assertEqual(format_word_list("adsfjkl a;lkdfjs wiuquq$"), ["adsfjkl", "alkdfjs", "wiuquq"])

class TestCheckWordList(unittest.TestCase):
    def test_single_correct_word(self):
        self.assertEqual(check_word_list("example"), "No Errors")

    def test_multiple_correct_words(self):
        self.assertEqual(check_word_list("tree example computer plus"), "No Errors")
    
    def test_single_incorrect_word(self):
        self.assertEqual(check_word_list("woarkz"), ["woarkz"])
    
    def test_correct_and_incorrect_words(self):
        self.assertEqual(check_word_list("Pthon is an excelllent language"), ["Pthon", "excelllent"])
    
    def test_with_special_characters(self):
        self.assertEqual(check_word_list("Pthon$ is an excelllent, language!!!"), ["Pthon", "excelllent"])
    
    def test_empty_string(self):
        self.assertEqual(check_word_list(""), "Empty String")
        
    def test_with_numbers(self):
        self.assertEqual(check_word_list("Python 3 is beter tkhan Python 2"), ['beter', 'tkhan'])

if __name__ == "__main__":
    unittest.main()