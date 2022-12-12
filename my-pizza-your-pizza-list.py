my_pizza = ['sausage delight', 'cheese blast', 'BBQ']
your_pizza = my_pizza[:]

my_pizza.append('pina-apple pizza')
your_pizza.append('tomatino pizza')

print('My pizzas: ')
for pizza in my_pizza:   # printing the list by using a for loop
    print('\t' + f'{pizza}')

print('Your pizzas: ')
for pizza in your_pizza:  # printing the list by using a for loop
    print('\t' + f'{pizza}')


