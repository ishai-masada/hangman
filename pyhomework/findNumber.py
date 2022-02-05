# Finding a number in a list
# Ishai Masada

count = 0
num_list = [1, 1, 3, 3, 5, 7, 9, 11, 13, 15, 17, 19]
requested_num = int(input("Type in an odd number betwee 0 and 20: "))
if requested_num not in num_list:
    print("You entered a number that is not in the list.")
while (requested_num in num_list):
    if count == 0:
        print(f'Position of the first occurance of the number in the list: {num_list.index(requested_num)}')
    num_list.remove(requested_num)
    print(requested_num)
    count += 1
