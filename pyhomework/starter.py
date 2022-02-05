# Wrestling Starter Function
# Ishai Masada

def starter():
    weight = float(input("Type in your weight: "))
    numWins = int(input("Type in the number of wins you have:"))
    if (weight >= 150) and (weight < 160) and (numWins >= 5):
        print("\nCongratulations! You are eligible to join the wrestling team!")
    elif (weight > 199) or (numWins > 20):
        print("\nCongratulations! You are eligible to join the wrestling team!")
    else:
        print("Sorry, you are not eligible to join the wrestling team.")
starter()
