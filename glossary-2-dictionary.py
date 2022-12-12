# crearing a dictionary
p_words = {
    'variable': 'To store a value',
    'list': 'Store sets of information',
    'loop': 'loop through every information to access it',
    'tuple': 'same as list but i cant be changed',
    'if-statement': 'to check a condition',
    'dictionary': 'has key and value',
    'list- comprehension': 'allows you to do all the work in the list'
}  # Here [p_words = programming word]

# using a for loop to get access to keys and values
for k,n in p_words.items(): # here [k -> Key] & [n -> values]
    print(k + '->' + '\t' + n + '\n')