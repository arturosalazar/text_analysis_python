# Text Analysis - Personal Project

## Goal

The goal of this project is to explore different ways to analyze text with Python

## Requirements

### Vowel Numbers - count the number of vowels in an input

1. Create a list of valid vowels (a, e, i, o, u)
2. Take in input from the user
3. Count the number of vowels in the user input
4. Return the number of vowels

### Word Numbers - count the number of words in an input

1. Take in input from the user
2. Count the number of spaces in the user input as way to indicate words
3. Return the number of words (i.e. spaces)

## Testing

Create Unit Tests for each file

### Vowel Numbers Test Cases:

1. Input with all vowels: To ensure the program accurately counts each type of vowel.
2. Input with no vowels: To check the program correctly returns zero when there are no vowels.
3. Mixed input (vowels and consonants): To verify the program can correctly identify and count only the vowels among other characters.
4. Case sensitivity: To ensure the program counts both uppercase and lowercase vowels.
5. Empty input: To see how the program handles an empty string.

### Word Numbers Test Cases:

1. Single word input: To verify that the program returns 1 when there's only one word.
2. Multiple words input: To check the program counts words correctly in a sentence.
3. Input with multiple spaces: Since words might be separated by more than one space, it's good to test that scenario.
4. Empty input: To determine how the program handles an empty string.
5. Input with punctuation: To see if punctuation affects the word count.
