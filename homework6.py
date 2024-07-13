import os
os.system("cls")

def func(d):
    if not d:
        print("Dictionary bo'sh")
        return

    max_value = max(d.values())
    
    print(f"Maksimal qiymat: {max_value}")

my_dict = {"k": 6, "o": 16, "m": 66, "o":106, "l": 166, "a": 666}

func(my_dict)
