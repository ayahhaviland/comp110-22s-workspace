"""EX03 - Wordle."""

__author__ = "730236204"

SECRET_WORD: str = ("codes")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Checking to see if inputted character is found in word."""
    assert len(char) == 1
    # variable to track index 
    i: int = 0
    # variable to track if character found in word
    found: int = 0
    while i < len(word):
        if(word[i] == char):
            found = 1  
        i = i + 1
    if(found == 1):
        return True
    else:
        return False


def emojified(secret: str, guess: str) -> str:
    """To print an emoji string reflecting guessed word."""
    assert len(guess) == len(secret)
    # variable to track index
    idx: int = 0
    # variable to show resulting emojis
    resulting_emoji: str = ""

    while idx < len(guess):
        if(guess[idx] == secret[idx]):
            resulting_emoji = resulting_emoji + GREEN_BOX
        else: 
            if contains_char(secret, guess[idx]):
                resulting_emoji = resulting_emoji + YELLOW_BOX
            else:
                resulting_emoji = resulting_emoji + WHITE_BOX
        idx = idx + 1
    return resulting_emoji


def input_guess(length: int) -> str:
    """Checking to see if word inputted is the same length of secret word."""
    # variable to track length of word guessed
    len_guess: str = input("Enter a " + str(length) + " character word: ")
    while len(len_guess) < length or len(len_guess) > length:
        len_guess: str = input("That wasn't " + str(length) + " chars! Try again: ")
    return len_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # variable to define max turn
    turns_max: int = 6
    # variable to track player's current turn
    turns_taken: int = 1
    # variable to track a win or lose 
    wrong_guess: bool = True
    while turns_taken < 7 and wrong_guess:
        print("=== Turn " + str(turns_taken) + "/" + str(turns_max) + " ===")  
        # variable to recieve input guess
        input_test: str = str(input_guess(len(SECRET_WORD)))
        # variable to recieve emoji string 
        test: str = str(emojified(SECRET_WORD, input_test))
        print(test)
        if SECRET_WORD == input_test:
            wrong_guess = False
        else:
            turns_taken += 1
    if wrong_guess:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print("You won in " + str(turns_taken) + "/" + str(turns_max) + " turns!")


if __name__ == "__main__":
    main()