# creating a list of orders
order = ['chicken sandwich', 'Egg sandwich', 'BBQ sandwich']
finished = []

# looping through order
while order:
    current = order.pop()
    print("I preparing your " + f'{current}' + ".")
    finished.append(current)

for sandwich in finished:
    print(sandwich)
