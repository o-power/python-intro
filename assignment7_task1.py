# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def can_convert_to_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# 1. Create an integer constant and assign to it the number to be guessed
NUMBER_TO_GUESS = 3
MAX_TRIES = 5

# 2. Create a Boolean flag called is_playing and initialize it as True (assign it the value True)
is_playing = True

# 3. Declare a variable called tries, initialize to 0 (zero)
tries = 0

# 4. Display a message to welcome the player and tell them to type quit if they want to end the game
message = "\nWelcome to the 'Guess that Number' game."
message += "\nType 'quit' at any time to end the game."
print(message)

# 5. Create a while loop with a compound condition – the loop should keep running while is_playing
#    is True and the player hasn’t had more than 5 tries
# 6. Tell the player how many tries they have left and invite them to input their guess (remember 
#    to cast the input to an integer)
# 7. Write an if-elif-else chain that tells the player if their guess is too high, too low, or 
#    is correct (you don’t need to handle the possibility of the wrong type of input)
# 8. Increment tries in the if-elif-else chain where appropriate
while is_playing and tries < MAX_TRIES:

    message = f"\nYou have {MAX_TRIES - tries} guess{'' if (MAX_TRIES-tries) == 1 else 'es'} left."
    message += "\nEnter your guess: "
    
    guess = input(message)
    guess = guess.strip()
    
    tries += 1

    if guess.lower() == "quit":
        is_playing = False
        print("\nYou have chosen to quit. Bye for now!")
    elif can_convert_to_int(guess):
        if int(guess) == NUMBER_TO_GUESS:
            is_playing = False
            print("\nWow! You have guessed the correct number!")
        elif int(guess) > NUMBER_TO_GUESS:
            if tries < MAX_TRIES:
                print("\nYou have guessed too high. Try again!")
            else:
                print("\nYou have guessed too high. You lose!")
        else:
            if tries < MAX_TRIES:
                print("\nYou have guessed too low. Try again!")
            else:
                print("\nYou have guessed too low. You lose!")
    else:
        print("\nYou must enter an integer!")

# 9. Lastly, display a message after the while loop to thank the user for playing
print("\nThanks for playing!")
