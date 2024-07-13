import os
os.system("cls")


def find_second_maximum(nums):    
    max1 = float('-inf')  
    max2 = float('-inf') 

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:  
            max2 = num

    return max2

nums = [3, 1, 7, 4, 5, 6]
result = find_second_maximum(nums)
print("Ikkinchi maksimum son:", result)



