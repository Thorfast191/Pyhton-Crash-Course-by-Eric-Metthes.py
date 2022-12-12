age = 22

# writing if-elif-else statement to check the condition
if age < 2:
    print('baby')
elif age == 2 or age < 4:
    print('toddler')
elif age == 4 or age < 13:
    print('kid')
elif age == 13 or age < 20:
    print('teenage')
elif age == 20 or age < 65:
    print('adult')
elif age > 65:
    print('elder')