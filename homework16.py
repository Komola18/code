import os
os.system("cls")

def func (item):
    if isinstance(item, int):
        return float(item)
    elif isinstance(item, float):
        return int(item)
    else:
        return item

number_list = [1, 2.5, 3, 4.0, 5, 6.7]

natija = list(map(func, number_list))

print(natija)
