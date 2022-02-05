# High-Low Game
# Ishai Masada
from random import randint

def hi_low():
    global guesses
    global answer
    num_range = range(1, 101)
    answer = randint(1, 100)
    guesses = 0
    result = False
    while (guesses<7):
        guess = int(input("Type in a number between 1 and 100: "))
        if guess < answer:
            print("Your guess was too low.")
            guesses += 1
        elif guess > answer:
            print("Your guess was too high.")
            guesses += 1
        else:
            print("You guessed the number!")
            result = True
            guesses += 1
            break
    print(f'guesses: {guesses}')
    return result

function_return = hi_low()
if function_return:
    print(f"You won with {guesses} guesses!")
elif function_return == False:
    print(f"Sorry, you lose. The answer was {answer}")
