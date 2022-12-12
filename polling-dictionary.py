# dictionary
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

person = ['arafat', 'jen', 'phil', 'anis'] # list

# using a for loop
for n in person:

    if n in favorite_languages.keys(): # checking condition
        print(n.title() + " Thank you for polling")

    else: print(n.title() + ' Please take the poll')