
"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730236204"

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

matching_characters = 0 

if character == word[0]:
    print(character + " found at index 0")
    matching_characters = matching_characters + 1

if character == word[1]:
    print(character + " found at index 1")
    matching_characters = matching_characters + 1

if character == word[2]:
    print(character + " found at index 2")
    matching_characters = matching_characters + 1

if character == word[3]:
    print(character + " found at index 3")
    matching_characters = matching_characters + 1

if character == word[4]:
    print(character + " found at index 4")
    matching_characters = matching_characters + 1

if matching_characters == 0:
    print("No instances of " + character + " found in " + word)
else:
    if matching_characters == 1:
        print("1 instance of " + character + " found in " + word)
if matching_characters == 2:
    print("2 instances of " + character + " found in " + word)
else:
    if matching_characters == 3:
        print("3 instances of " + character + " found in " + word)
if matching_characters == 4:
    print("4 instances of " + character + " found in " + word)
else:
    if matching_characters == 5:
        print("5 instances of " + character + " found in " + word)