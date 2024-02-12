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

if __name__ == "__main__":
    user_input = input("Please provide a string: ")
    print(is_valid_word_nltk(user_input))