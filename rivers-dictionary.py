# creating a dictionary
river_country = {
    'Nile': 'Egypt',
    'Padma': 'Bangladesh',
    'Jamuna': 'India'
}

# using a loop to print a sentence
for k,n in river_country.items():
    print(k + 'runs through' + n)

print('\n') # break the line

# using a for loop to print each name of the river
for k in river_country.keys():
    print(k)

print('\n') # break the line

# using a for loop to print each of the country the river runs through
for n in river_country.values():
    print(n)