
nums = ['0010', '1011', '1001', '1001']

most_common = '1'
least_common = '0'

# o2
nums = [num for idx, num in enumerate(nums) if num[idx] == most_common]
print(nums)
