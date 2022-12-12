# while not equal to quit
while True:
    age = input("How old are you? or type quit to exit: ")
    if age == 'quit':
        break
    if int(age) < 3 :
        print("ticket is free")
        break
    if int(age) >= 3 and int(age) <= 12:
        print("Ticket costs $10")
        break
    if int(age) > 12 :
        print("Ticket costs $15")
        break