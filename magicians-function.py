def show_magicians(names): # we defined a function with parameter names
    for name in names: # then we looped through names
        msg = "some magicians name: " + name # store names in a variable
        print(msg) # print 

magician_names = ['david copperfield', 'doug henning', 'david blane'] # created a list
show_magicians(magician_names) #calling function using the names in the list