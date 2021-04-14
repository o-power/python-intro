"""Hangman

This module provides the functions for a hangman game.
"""

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
            print('Your guess must be a single letter. Try again!\n')
        else:
            is_guessing = False
            return_value = guess
        
    return return_value

def add_correct_guess(player_guess, round_progress, word_to_guess):
    """Replaces the underscores in round_progress with the player_guess
    for all instances of player_guess in word_to_guess.

    Parameters:
    player_guess (str): a letter which is in word_to_guess.
    round_progress (list): a list of letters and underscores.
    word_to_guess (list): a list of letters representing the word to guess.
    """
    letter_count = 0

    for letter in word_to_guess:
        if letter == player_guess:
            round_progress[letter_count] = player_guess
        letter_count += 1

def round_won(word_to_guess):
    """Displays a congratulations message and the word."""
    print("Congrats! You have guessed all the letters!")
    display_word(word_to_guess)
