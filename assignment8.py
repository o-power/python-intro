
# c) Create a loop that will prompt the user to input a word until the user types ‘stop’

# e) If the player types ‘stop’ the loop should end
# f) The function returns a nested list of words


def get_words():
    """Returns a list of user inputted words.

    Returns:
    words (list): A list of words where each word is itself
                  a list of the uppercase letters in the word.
    """
    message = "\nEnter the word(s) to guess."
    message += "\nType 'stop' when done.\n"
    print(message)

    is_entering_words = True
    message = "Enter a word: "
    words = []

    while is_entering_words:
        word = input(message).strip()
        if word.lower() == "stop":
            is_entering_words = False
        else:
            words.append(list(word.upper()))

    return words

def display_word(word):
    """Displays the word.
    
    Parameters:
    word (list): a list of letters or underscores.
    """
    for letter in word:
        print(letter, end="")

    print()

def get_guess():
    """Gets the user's guess for one of the letters.

    Returns:
    return_value (str): None if user quit; otherwise the user's guess.
    """
    is_guessing = True
    message = "Enter a guess: "
    return_value = ""

    while is_guessing:
        guess = input(message).strip().upper()
        if guess == "QUIT":
            is_guessing = False
            return_value = None
        elif len(guess) > 1:
            print('Your guess must be a single letter. Try again!')
        else:
            return_value = guess
        
    return return_value

def main():
    """Runs the game.
    """
    message = "\nWelcome to the 'Hangman' game."
    print(message)

    words = get_words()
    print(words)

    is_playing_game = True
    game_round = 0
    guessed_letters = []

    while is_playing_game and game_round < len(words):
        is_playing_round = True
        word_to_guess = words[game_round]
        round_progress = ['_ ' for letter in word_to_guess]

        message = f"\nThe word to guess has {len(word_to_guess)} letters."
        message += "\nType 'quit' at any time to end the round."
        print(message)

        while is_playing_round:
            display_word(round_progress)
            guess = get_guess()
            print(guess)
            break

        game_round += 1

    print("\nThanks for playing!")
    print(get_words.__doc__)

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()