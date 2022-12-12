import json

def fav_number():
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        fav_num = input("What is your favourite number? ")
        with open(filename, 'w') as f_obj:
            json.dump(fav_num, f_obj)
            print("My favourite number is " + fav_num)
    else:
        print( fav_num + "!")
fav_number()