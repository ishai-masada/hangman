# Day 3 | Part 1
# Submarine Status Repot
# Ishai Masada

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

bin_nums = re.findall(r'(\d+)', bin_nums)
digits = []

for _ in range(0, len(bin_nums[0])):
    digits.append([])

for num in bin_nums:
    for idx, digit in enumerate(digits):
        digit.append(num[idx])

gamma = []
epsilon = []
for digit in digits:
    if digit.count('1') > digit.count('0'):
        digit.clear()
        gamma.append('1')
        epsilon.append('0')
    elif digit.count('1') < digit.count('0'):
        digit.clear()
        gamma.append('0')
        epsilon.append('1')

power = int(''.join(gamma), 2) * int(''.join(epsilon), 2)
print(power)
