flag = True # creating flag

names = [] # empty list to store the names
file_name = "guest_book.txt" # creating a file object

while flag: # while loop
    names = input("Enter Your name: ") # taking input
    print("Greetings, " + names)

    with open(file_name,'w') as file_object: # writing to the file
        file_object.write(names)
        print('Your name hase been recorder.')

    exit = input("Press 'q' to Exit! or press 'p' to continue")

    if exit == 'q':
        break
    if exit == 'p':
        continue

