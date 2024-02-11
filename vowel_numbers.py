# Count the number of vowels in a user's input

def count_vowels(user_input):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0

    for char in user_input:
        if char in vowels:
            counter += 1

    return counter

if __name__ == '__main__':
    user_input = input("Please provide a string: ")
    print(count_vowels(user_input))