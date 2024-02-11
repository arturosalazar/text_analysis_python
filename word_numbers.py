# Count the number of words in a user's input

def count_words(user_input):
    words = user_input.split(" ")
    # Remove any empty strings (indicator of extra spaces in input)
    words = list(filter(None, words))
    return len(words)
    
if __name__ == "__main__":
    user_input = input("Please provide a string: ")
    print(count_words(user_input))