import os
import random
import time


def clear():
	os.system('clear')

percent_bar = ''
for i in range(10):
    percent_bar += '-'

clear()
percent = 0
while percent < 100:

    # Display the percentage and the loading message
    print(round(min(percent, 100), 2),  '%', " loading...")
    time.sleep(random.randrange(3))
    clear()

    # Increment the percentage by a random number
    decimal = random.randrange(9)/10
    integer = random.randrange(10)
    increment = decimal + integer
    percent += increment
