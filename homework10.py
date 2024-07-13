import os
os.system("cls")

def func(d):
    my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

    for key in list(my_dict.keys()):  
            del d[key]

    qoldiq_value = list(my_dict.values())
    print("Qolgan valuelar:", qoldiq_value)

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
func(my_dict)
