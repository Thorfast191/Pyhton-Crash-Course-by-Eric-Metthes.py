try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
except ValueError:
    print("You cant enter non integer value: ")
else:
    print(a + b)