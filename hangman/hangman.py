import random

# This is a hangman game


# Part I: Assignment:
# Write a program to support the children's spelling game hangman. Call the program hangman.py. Since there are
# many versions of hangman, be sure that you implement exactly the following.
# The player is to guess the letters in a secret word. Use underscores to display the number of letters in the word.
# When the player guesses a correct letter, display the word with that letter showing. Correct guesses don't count
# against the player. Incorrect guesses count, and the player loses on the seventh incorrect guess. Each time the player
# is asked to enter a letter, the program should display how many guesses they have left and a list of all of the
# incorrect letters they have guessed.  If the player accidentally chooses a letter that has already been guessed, this
# should not count as a guess.  See sample games below.
# Your program must contain at least the following functions. (If you want you may use other functions as well.)
#  A function that gets a list of words from a file.  Call the file wordlist.txt.  You must provide your own
# when you test your program.
#  A function that randomly picks a secret word from the list.
#  A function that plays the game (i.e., other than main()).
#  A function that displays the blanked-out secret word.
#  A function that determines whether the letters that have been entered spell the secret word (this returns a
# boolean).

# Part II: User Interface (optional Extra Credit)
# Once you get your functions working with text, you can add a graphical user interface of your design.  The GUI
# should have the following elements:
#  A text area where the word with underscores representing the letters of the word is presented.
#  A text area where the letters used are displayed.  Optionally you can display the letters not chosen yet.  In
# either case you must identify which role the letters displayed serve.
#  A text area indicating the number of guesses the user has remaining.
#  An area where the user enters the letter s/he wishes to play.
#  When a game completes, a message should appear in the GUI window asking the player whether they want
# to play another game.  The GUI should also provide Yes and No buttons for the player to make a choice.
# Once your basic program is working:
# The traditional way to play hangman is to draw a figure on a gallows. Another part of the hanged man is added for
# each incorrect guess. When the figure is complete, the player loses. How you draw the figure is up to you, but it
# should have exactly seven parts.
# Submission:
# Submit finished program to the appropriate dropbox.  You will have two weeks to work on this program.

import random
def load_file():

    # Load in the word list from the .txt file
    global word_list
    word_list = []
    with open("wordlist.txt", 'r') as f:
        for word in f:
            word_list.append(word)

    return word_list

def generate_word(list_of_words):

    # Pick a random word from the list of words
    answer = random.choice(list_of_words)

    # Making sure that the word is 7 letters or less
    while len(answer) > 7:
        answer = random.choice(list_of_words)

    return answer

def get_guess(letter_position):

    # Make a while loop to ask the player for a correct answer until they give a valid response
    while True:
        guess = input(f"\nGuess letter {letter_position+1}: ")

        # Check if the length of the input was not 1
        if len(guess) != 1:
            print("\nEach guess must be a single letter, only.")

        # Check if the type of the input is an integer
        elif guess.isnumeric():
            print("\nEach guess must be a single letter, only.")
        else:
            break

    return guess

def verify_guess(guess, answer, index):

    # Check if the guess is equal to the letter in the answer
    if guess == answer[index]:
        print("\nYou guessed the correct letter!")
        return True
    else:
        print("\nYou guessed an incorrect letter!")
        return False

def display(guesses, answer):
    global correct_letters
    global incorrect_letters

    #These are the correct letters
    correct_letters = []

    # These are the incorrect letters
    incorrect_letters = []

    answer = list(answer)

    # Fill the display list with the amount of underscores as there are letters in the answer
    for _ in range(0, len(answer)):
        correct_letters.append('_')

    # Iterate over the answer and geusses simultaneously to check each guess
    for idx, group in enumerate(zip(answer, guesses)):
        letter = group[0]
        guess = group[1]
        if letter == guess:
            correct_letters.insert(idx, guess)
            correct_letters.remove(correct_letters[idx+1])
        else:
            incorrect_letters.append(guess)

    results = [correct_letters, incorrect_letters]
    return results

# Load in the list of words
load_file()

# Pick a random word from the list of words
answer = generate_word(word_list).strip()

number_of_guesses = 7

# This is a list of the player's guesses
total_guesses = []

# This is the number of letters that the player has guessed correctly
answer_progress = 0

while True:
    print(f"\nNumber of guesses left: {number_of_guesses}")

    #Check if the guessed letters equals the word
    if ''.join(total_guesses) == answer:
        print("\nYou guessed the word! You win!")
        break

    #Check if the player has run out of guesses
    elif number_of_guesses <= 0:
        print("\nYou were not able to guess the word! You lose!")
        break

    # Get the player's guess
    guess = get_guess(answer_progress)

    # Put the guess in the list of guesses
    total_guesses.append(guess)

    # Check if the guessed letter is the next letter in the word
    elif verify_guess(guess, answer, answer_progress):
        answer_progress += 1

    print('\n')
    results = display(total_guesses, answer)
    # print(' '.join(results[0]))
    # print('\n')
    # print(' '.join(results[1]))
    number_of_guesses -= 1
