# Counting the number of digits in a number
# Ishai Masada
import copy

def count_digits():
    num = 1
    while (num>0):
        count = 0
        # Take the input as an integer and put it into a list
        num = int(input("Type in a number greater than zero: "))
        if num<=0:
            continue
        num_list = []
        num_list.append(num)
        # Copy the number to use for calculations
        copy_num = copy.deepcopy(num_list)[0]
        while True:
            copy_num = copy_num//10
            count += 1
            if copy_num == 0:
                break
        print(f'There are {count} digit(s) in the number entered')
    print("The number you entered was not greater than zero.")

count_digits()
