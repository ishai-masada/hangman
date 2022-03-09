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

# Ask the player to guess a letter
def get_guess():

    # Make a while loop to ask the player for a correct answer until they give a valid response
    while True:
        guess = input(f"\nGuess a letter in the word: ")

        # Check if the length of the input was not 1
        if len(guess) != 1:
            print("\nEach guess must be a single letter, only.")

        # Check if the type of the input is an integer
        elif guess.isnumeric():
            print("\nEach guess must be a single letter, only.")
        else:
            break

    return guess

# Check if the player's guess was correct
def verify_guess(answer, answer_progress, correct_guesses, incorrect_guesses, \
                 guess):

    results = [correct_guesses, incorrect_guesses, answer_progress]

    # Check if the guess is equal to the letter in the answer
    if guess in answer:
        print("\nYou guessed a correct letter!")
        if correct_guesses.count(guess) < answer.count(guess):
            correct_guesses.append(guess)
            answer_progress += 1
    else:
        print("\nYou guessed an incorrect letter!")
        incorrect_guesses.append(guess)

    return results

# Display correct and incorrect guesses to the user
def display(blank_answer, results=list):

    correct_guesses = ' '.join(results[0])
    incorrect_guesses = ' '.join(results[1])
    print(blank_answer)
    print(f'\nincorrect_guesses: {incorrect_guesses}')
    print(f'correct_guesses: {correct_guesses}')

def verify_answer(correct_guesses, answer):
    if sorted(correct_guesses) == sorted(answer):
            print("\nYou guessed the word! You win!")
            return True

def hangman():
    # Load in the list of words
    load_file()

    # Pick a random word from the list of words
    answer = generate_word(word_list).strip()
    blank_answer = ' '.join(['_' for letter in answer])

    # Number of chances that the player has to guess the word
    number_of_guesses = 7

    correct_guesses = []
    incorrect_guesses = []

    # This is the number of letters that the player has guessed correctly
    answer_progress = 0

    while True:

        print(f"\nNumber of guesses left: {number_of_guesses}")

        #Check if the guessed letters equals the word
        if verify_answer(correct_guesses, answer):
            break

        #Check if the player has run out of guesses
        elif number_of_guesses <= 0:
            print("\nYou were not able to guess the word! You lose!")
            break

        guess = get_guess()

        # Verify the player's guess with the verify function and store the results into a variable
        results = verify_guess(answer, answer_progress, correct_guesses, incorrect_guesses, \
                               guess)

        # Display information to the user
        display(blank_answer, results)

        number_of_guesses -= 1

if __name__ == "__main__":
    hangman()
