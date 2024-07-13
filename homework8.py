import os
os.system("cls")

def func(d):

    result_set = set()
    
    for key, value in d.items():
        result_set.add((key, value)) 
    
    return result_set

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

result_set = func(my_dict)
print("Dictionary dan olingan set:", result_set)
