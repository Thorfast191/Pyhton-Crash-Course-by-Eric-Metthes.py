# function to make shirt
def make_shirt(size,message):
    print("T-shirt size: " + str(size) + '\n' + "message that will print on the shirt: " + message)

make_shirt(20,"fuck uo") # calling the function by using positional argument
make_shirt(size=20,message="fuck uo") # calling the function by keyword argument