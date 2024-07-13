import os
os.system("cls")

def func(nums):
    max_even = -1
   
    for i in nums:
        if i % 2 ==0:
            if i > max_even:
                max_even = i

    return max_even


nums=[1,2,3,4,5,6,]

func(nums)

print(func(nums))