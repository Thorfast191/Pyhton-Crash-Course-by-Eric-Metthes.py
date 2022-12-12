flag = True # creating a flag

names = [] # creating a empty list
reason = []

file_name = "reason.txt"

while flag:
    names = input("Enter your name: ") # taking names, reason as input
    reason = input("Why do you love programming?")

    print("My name is " + names + "  and my reason is, " + reason) # printing

    with open(file_name,'w') as file_object: # writing to the file
        file_object.write(names + reason)

    next =  input("Press 'q' to Exit or Press 'p' to continue if anyone left to answer")

    if next == 'q':
        flag = False
    if next == 'p':
        continue
