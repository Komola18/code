import os
os.system("cls")

def func(d):
    for key in d:
        d[key] = 0


my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}


func(my_dict)


print("Yangilangan dictionary:", my_dict)
