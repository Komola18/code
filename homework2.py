import os
os.system("cls")


def find_second_min(nums):    
    min1 = float('inf')  
    min2 = float('inf') 

    for num in nums:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:  
            min2 = num

    return min2

nums = [3, 1, 7, 4, 5, 6]
result = find_second_min(nums)
print("Ikkinchi mion son:", result)
