# Lab 6
# Ishai Masada
# Function Practice

def sumN(n):
    nat_nums = [n]
    for num in range(n):
        nat_nums.append(num)
    print(f'Sum of the numbers in {n}: {sum(nat_nums)}')

def sumNCubes(n):
    nat_nums = [n**3]
    for num in range(n):
        nat_nums.append(num**3)
    print(f'Sum of the cubes of the first {n} natural numbers: {sum(nat_nums)}')

def rec_area(length, width):
    area = length*width
    print(f'Area: {area}')

def squareEach(nums):
    for index, num in enumerate(nums):
        nums[index] = num**2
    print(f'Squared number list: {nums}')

def sumList(nums):
    print(f'Sum of the list: {sum(nums)}')

sumN(7)
sumNCubes(2)
rec_area(3, 4)
squareEach([2, 4, 5])
sumList([2, 3, 4])
