# Count the number of vowels in a user's input

vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0

user_input = input("Please provide a string: ")

for char in user_input:
    if char in vowels:
        counter += 1

print(counter)