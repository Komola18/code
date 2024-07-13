import os
os.system("cls")

def func(item):
    return isinstance(item, str)

string_list = ['komola', 'abdurasulova','abdulaziz qizi',] 

filtr = list(filter(func, string_list))

print(filtr)

