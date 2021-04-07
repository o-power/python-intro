
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
    player_guess (): a letter which is in word_to_guess.
    round_progress (list): a list of letters and underscores.
    word_to_guess (list): a list of letters representing the word to guess.
    """
    letter_count = 0

    for letter in word_to_guess:
        if letter == player_guess:
            round_progress[letter_count] = player_guess
        letter_count += 1

def round_won(word_to_guess):
    """Displays a congratulations message and the word.
    """
    print("Congrats! You have guessed all the letters!")
    display_word(word_to_guess)
    
def main():
    """Runs the game.
    """
    message = "\nWelcome to the 'Hangman' game."
    print(message)

    words = get_words()
    #print(words)

    is_playing_game = True
    game_round = 0
    guessed_letters = []

    while is_playing_game and game_round < len(words):
        is_playing_round = True
        word_to_guess = words[game_round]
        round_progress = ['_ ' for letter in word_to_guess]

        message = f"\nThe word to guess has {len(word_to_guess)} letters."
        message += "\nType 'quit' at any time to end the game.\n"
        print(message)

        while is_playing_round:
            display_word(round_progress)
            guess = get_guess()
            if guess is None:
                is_playing_game = False
                break
            elif guess in guessed_letters:
                print("You have already guessed this letter. Guess again!\n")
            elif guess not in word_to_guess:
                print(f"Unlucky! The letter {guess} is not in the word.\n")
                guessed_letters.append(guess)
            else:
                print(f"Correct! The letter {guess} is in the word.\n")
                add_correct_guess(guess, round_progress, word_to_guess)
                guessed_letters.append(guess)
                if '_ ' not in round_progress:
                    round_won(word_to_guess)
                    is_playing_round = False
                    game_round += 1
                    word_to_guess.clear()
                    round_progress.clear()
                    guessed_letters.clear()
                
    print("\nThanks for playing!")
    #print(get_words.__doc__)

if __name__ == "__main__":
    # Code in here will only execute when the file is run directly    
    main()