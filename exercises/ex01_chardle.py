"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730236204

word: str = input("Enter a 5-character word: ")

if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    if len(word) > 5:
        print("Error: Word must contain 5 characters")
        exit()

character: str = input("Enter a single character: ")

if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()
else:
    if len(character) > 1:
        print("Error: Character must be a single character.")
        exit()

print("Searching for " + character + " in " + word)

number_of_matching_variables = 0 

if character == word[0]:
    print(character + " found at index 0")
    number_of_matching_variables = number_of_matching_variables + 1

if character == word[1]:
    print(character + " found at index 1")
    number_of_matching_variables = number_of_matching_variables + 1

if character == word[2]:
    print(character + " found at index 2")
    number_of_matching_variables = number_of_matching_variables + 1

if character == word[3]:
    print(character + " found at index 3")
    number_of_matching_variables = number_of_matching_variables + 1

if character == word[4]:
    print(character + " found at index 4")
    number_of_matching_variables = number_of_matching_variables + 1

if number_of_matching_variables == 0:
    print("0 instances of " + character + " found in" + word)
else:
    if number_of_matching_variables == 1:
        print("1 instance of " + character + " found in" + word)
    else: 
        print(number_of_matching_variables, " instances of " + character + " found in " + word)