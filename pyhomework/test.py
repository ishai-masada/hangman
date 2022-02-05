# Replit stuff or other stuff
# Ishai Masada

nums = [str(num) for num in input().split()]
count = 0

for idx, num in enumerate(nums):
    print(num)
    if count%2 != 0:
        count += 1
        continue
    try:
        if len(nums)%2 == 0:
            removed_element = nums.pop(idx+1)
            nums.insert(idx, removed_element)
        elif idx == nums.index(nums[-2]) and len(nums)%2 != 0:
            break
        elif len(nums)%2 != 0:
            removed_element = nums.pop(idx+1)
            nums.insert(idx, removed_element)
    except:
        removed_element = nums.pop(idx)
        nums.insert(idx+1, removed_element)
    count += 1

print(' '.join(nums))
