import os
os.system("cls")

def func(d):
    if not d:
        print("Dictionary bo'sh")
        return

    max_key = max(d.keys())
    
    print(f"Maksimal qiymat: {max_key}")

my_dict = {1: 6, 2: 16, 3: 66, 4:106, 5: 66, 6: 666}

func(my_dict)
