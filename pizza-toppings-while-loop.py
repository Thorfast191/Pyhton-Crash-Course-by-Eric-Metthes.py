n_topping = '' # empty string

# add topping until  == 'quit'
while n_topping != 'quit':
    n_topping = input("what topping would you like for your pizza?\n"
                      + "or Enter quit to exit")
    if n_topping != 'quit':
        print("Adding " + n_topping + " to your pizza.")