# creating a list of orders
order = ['Pastrami', 'chicken sandwich', 'Pastrami', 'Egg sandwich', 'BBQ sandwich', 'Pastrami']
finished = []

print("We are out of pastrami sandwich sorry.")

# looping through order to remove pastrami
while 'Pastrami' in order:
    order.remove('Pastrami')

# while loop to append order into finished
while order:
    current = order.pop()
    finished.append(current)

#for loop to print finished
for sandwich in finished:
    print(sandwich)