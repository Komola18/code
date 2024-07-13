import os
os.system("cls")

def func(dct):
    swapped_dct = {v: k for k, v in dct.items()}
    print(swapped_dct)



dct = {
    'a': 1,
    'b': 2,
    'c': 3
}

func(dct)