# Forcing good input
# Ishai Masada

def input_good_stuff():
    valid_input = range(1, 11)
    user_in = 0
    while (user_in not in valid_input):
        user_in = int(input("Type in a number between 1 and 10, including 10: "))
        print("Your input was not valid, it was not a number between 1 and 10")
    print(f"Hooray! You entered in a valid input! Your input: {user_in}") 

input_good_stuff()
