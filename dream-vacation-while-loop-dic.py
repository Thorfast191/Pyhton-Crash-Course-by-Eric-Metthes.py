dream_vac = {}
active_pollintg = True # creating a flag

while active_pollintg:
    name = input("What is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")

    dream_vac[name] = location # storing into the dictionary

    other_response = input("Anyone else who want to answer? ")

    if other_response.title() == 'No':
        active_pollintg = False

for name,location in dream_vac.items(): # for loop through dictionary to print
    print(name.title() + " would like to visit " + location.title())