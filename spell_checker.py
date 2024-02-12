# Check that user's input is correct 

# Import nltk library, download 'words' corpus containing all of the words 
#  to test against. 
# Download 'words' method from nltk.corpus to use 'words corpus'
# Add all words in corpus to a set for faster look up as spell checker

# corpus - a large and structured set of text, used for linguistic research, 
#  analysis, and developing nlp models. They serve as a comprehensive database
#  of language

import string
import nltk
nltk.download('words') 
from nltk.corpus import words

word_list = set(words.words())

def is_valid_word_nltk(word):
    return word.lower() in word_list

def check_word_list(user_input):
    if not user_input:
        return "Empty String"
    input_words_list = format_word_list(user_input)
    error_words = []
    for word in input_words_list:
        if not is_valid_word_nltk(word):
            error_words.append(word)

    if error_words:
        return error_words
    else:
        return "No Errors"

"""Format words into a list of just strings without punctuation"""
def format_word_list(input_string):

    # Remove any numbers
    translation_table_num = str.maketrans('', '', string.digits)
    text_no_numbers = input_string.translate(translation_table_num)
    
    # Remove any punctuation
    translation_table_punctuation = str.maketrans('', '', string.punctuation)
    text_no_punctuation = text_no_numbers.translate(translation_table_punctuation)
    
    input_words_list = text_no_punctuation.split(" ")
    input_words_list = list(filter(None, input_words_list))
    return input_words_list


if __name__ == "__main__":
    user_input = input("Please provide a string: ")
    print(check_word_list(user_input))