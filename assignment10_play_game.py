import assignment10_hangman as hm
from random import shuffle

message = "\nWelcome to the 'Hangman' game."
print(message)

words = hm.get_words()
#print(f"Before shuffle: {words}")
shuffle(words)
#print(f"After shuffle: {words}")

is_playing_game = True
game_round = 0
guessed_letters = []

while is_playing_game and game_round < len(words):
    is_playing_round = True
    word_to_guess = words[game_round]
    #print(word_to_guess)
    round_progress = ['_ ' for letter in word_to_guess]

    message = f"\nThe word to guess has {len(word_to_guess)} letters."
    message += "\nType 'quit' at any time to end the game.\n"
    print(message)

    while is_playing_round:
        hm.display_word(round_progress)
        guess = hm.get_guess()
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
            hm.add_correct_guess(guess, round_progress, word_to_guess)
            guessed_letters.append(guess)
            if '_ ' not in round_progress:
                hm.round_won(word_to_guess)
                is_playing_round = False
                game_round += 1
                word_to_guess.clear()
                round_progress.clear()
                guessed_letters.clear()
            
print("\nThanks for playing!")