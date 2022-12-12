flag = True

while flag:
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))

    except ValueError:
        print("Not a valid input!!")

    else:
        c = a + b
        print(c)

    exit = input("Press 'q' to EXIT!! Or Press 'p' to continue.")

    if exit == 'q':
        flag = False
    if exit == 'p':
        continue