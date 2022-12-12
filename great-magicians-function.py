def show_magicians(magicians): # we defined a function with parameter names
    for magician in magicians: # then we looped through names
        msg = "some magicians name: " + magician # store names in a variable
        print(msg)

def make_great(magicians): #to add great to each  name
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + 'The great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magician_names = ['david copperfield', 'doug henning', 'david blane'] # created a list
show_magicians(magician_names) #calling function using the names in the list
make_great(magician_names)
show_magicians(magician_names)