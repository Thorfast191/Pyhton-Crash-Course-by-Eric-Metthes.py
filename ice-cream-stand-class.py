class Restaurant(): # creating a class
    def __init__(self, name , type):
        self.name = name
        self.type = type

    def describe_res(self):
        print("The name of this restaurant is " + self.name.title() +
              '\n' + "This is a " + self.type.title() + " restaurant")

    def status(self):
        print(self.name.title() + " is open.")

class IcecreamStand(Restaurant): # sub_class of Restaurant
    def __init__(self, name, type='Ice-cream'):
        super().__init__(name,type) # connects child-class to parent-class
        self.flavours = [] # creating a attribute for flavours

    def flavour_names(self): # shows the flavour name
        for name in self.flavours:
            print("The flavour of this ice cream is " + name.title() + '.')


restaurant = Restaurant('Vooter adda', 'chinesse') # creating instance of the class Restaurant
ice_cream_stand = IcecreamStand("Polar") # creating instance of the sub_class
ice_cream_stand.flavours = ['chocolate', 'vanilla'] # assigning the names of the flavour

print(restaurant.name.title() + " " + restaurant.type.title())

# calling methods
restaurant.describe_res()
restaurant.status()
ice_cream_stand.flavour_names()