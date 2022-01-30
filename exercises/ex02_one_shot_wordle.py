"""EX02 - One Shot Worldle."""

__author__ = "730236204"

SECRET_WORD: str = ("python")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input("What is your 6-letter guess? ")

while len(guess) < 6 or len(guess) > 6:
    guess: str = input("That was not 6 letters! Try again: ")

# variable to track index
i: int = 0
resulting_emoji: str = ""

while i < len(guess):
    if(guess[i] == SECRET_WORD[i]):
        resulting_emoji = resulting_emoji + GREEN_BOX
    else: 
        character_in_guess: bool = False
        # variable to track secret
        s: int = 0
        while s < len(SECRET_WORD) and not character_in_guess:
            if(guess[i] == SECRET_WORD[s]):
                character_in_guess: bool = True
            else:
                s = s + 1
        if character_in_guess:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
    i = i + 1
print(resulting_emoji)

if guess == SECRET_WORD:
    print("Woo! You got it!")

if guess != SECRET_WORD:
    print("Not quite. Play again soon!")