numbers = list(range(1,11)) # creating a list
print(numbers)
print('\n')

print('First three numbers are ' + f'{numbers[:3]}') # printing first three numbers of the list
print('\n')

half_numbers = int(len(numbers) / 2) # finding the middle point of a list
middle = numbers[half_numbers:]     # storing it into another temporary list
print('First three numbers from the middle: ' + f'{middle[:3]}')  # then slicing it from the middle
print('\n')

print('Last three numbers: ' + f'{numbers[-3:]}') # printing last three numbers
