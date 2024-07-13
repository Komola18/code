import os
os.system("cls")

def func(item):
    return bool(item)

binary_list = [1, 0, 1, 1, 0, 0, 1]

boolean_list = list(map(func, binary_list))

print(boolean_list)