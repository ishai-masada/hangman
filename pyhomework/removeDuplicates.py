# Remove Duplicates from a List
# Ishai Masada

def removeDuplicates(someList):
    someList = list(set(someList))
    print(someList)

removeDuplicates([1, 5, 5, 6, 6, 3, 3, 2, 5, 3, 1])
