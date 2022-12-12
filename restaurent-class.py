class Restaurant(): # creating a class
    def __init__(self, name , type):
        self.name = name
        self.type = type

    def describe_res(self):
        print("The name of this restaurant is " + self.name.title() +
              '\n' + "This is a " + self.type.title() + " restaurant")

    def status(self):
        print(self.name.title() + " is open.")

restaurant1 = Restaurant('Vooter adda', 'chinesse') # creating instance of the class Restaurant
restaurant2 = Restaurant('china sizzling', 'chinesse')
restaurant3 = Restaurant('K.F.C', 'fast food')


print(restaurant1.name.title() + " " + restaurant1.type.title())
print(restaurant2.name.title() + " " + restaurant2.type.title())
print(restaurant3.name.title() + " " + restaurant3.type.title())


restaurant1.describe_res() # calling methods
restaurant1.status()
restaurant2.describe_res() # calling methods
restaurant2.status()
restaurant3.describe_res() # calling methods
restaurant3.status()