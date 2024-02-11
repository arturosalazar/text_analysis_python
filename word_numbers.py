# Count the number of words in a user's input

counter = 0

user_input = input("Please provide a string: ")

# Only update counter if there is actually input, otherwise input 0 if empty str
if user_input:
    counter += 1
    for char in user_input:
        if char == ' ':
            counter += 1

print(counter)