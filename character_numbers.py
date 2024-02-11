# Count the number of characters in a user's input

def count_characters(user_input):
    return len(user_input)


if __name__ == "__main__":
    user_input = input("Please provide a string: ")
    print(count_characters(user_input))