# Count the number of words in a user's input

def count_words(user_input):
    counter = 0

    # Only update counter if there is actually input, otherwise input 0 if empty str
    if user_input:
        counter += 1
        for char in user_input:
            if char == ' ':
                counter += 1

    return counter

if __name__ == "__main__":
    user_input = input("Please provide a string: ")
    print(count_words(user_input))