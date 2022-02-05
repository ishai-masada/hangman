# Day 3 | Part 1
# Submarine Status Repot
# Ishai Masada

# Next time iterate over bin_nums backwards
import re

with open('num_list.txt', 'r') as f:
    bin_nums = f.read()

# bin_nums = '''
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''

bin_nums = [num for num in bin_nums.splitlines() if num]
digits = []
nums = []

for _ in range(0, len(bin_nums[0])):
    digits.append([])

def o2(digits, bin_nums):
    for idx, digit in enumerate(digits):
        if len(bin_nums) == 1:
            break

        # If the number of 1s is greater than the number of 0s, keep the numbers with a 1 in
        # the current position
        if digit.count('1') > digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']

        # If the number of 1s is less than the number of 0s, keep the numbers with a 0 in
        # the current position
        elif digit.count('1') < digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']

        # If the number of 1s is equal to the number of 0s, keep the numbers with a 1 in
        # the current position
        elif digit.count('1') == digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']

        # Remove all numbers from each digit in digits
        for digit in digits:
            digit.clear()

        # Append each digit from each position of each number in bin_nums
        for num in bin_nums:
            for idx, digit in enumerate(digits):
                digit.append(num[idx])

    o2 = int(bin_nums[0], 2)
    return o2


def co2(digits, bin_nums):
    for idx, digit in enumerate(digits):
        if len(bin_nums) == 1:
            break

        # If the number of 1s is greater than the number of 0s, keep the numbers with a 1 in
        # the current position
        if digit.count('1') < digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '1']

        # If the number of 1s is less than the number of 0s, keep the numbers with a 0 in
        # the current position
        elif digit.count('1') > digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']

        # If the number of 1s is equal to the number of 0s, keep the numbers with a 1 in
        # the current position
        elif digit.count('1') == digit.count('0'):
            bin_nums = [num for num in bin_nums if num[idx] == '0']

        # Remove all numbers from each digit in digits
        for digit in digits:
            digit.clear()

        # Append each digit from each position of each number in bin_nums
        for num in bin_nums:
            for idx, digit in enumerate(digits):
                digit.append(num[idx])

    co2 = int(bin_nums[0], 2)
    return co2

o2 = o2(digits, bin_nums)
co2 = co2(digits, bin_nums)


life_support_rating = co2*o2
print(life_support_rating)
