import os
os.system("cls")

def func(nums):
    
    return min(set(nums), key=nums.count)

nums = [3, 1, 7, 4, 5, 6, 1, 7, 7, 5, 7]
result = func(nums)
print("Eng kam qatnashgan sonlar:", result)