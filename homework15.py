import os
os.system("cls")

def func(item):
    return isinstance(item, (int, float)) and item > 0

number_list = [-5, 3, 0, -2.5, 4.6, -1, 7]

natija = list(filter(func, number_list))


print(natija)

