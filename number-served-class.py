class Restaurant(): # creating a class

    def __init__(self, name , type): # initialize attributes
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_res(self): # describes the restaurant
        print("The name of this restaurant is " + self.name.title() + "."
              '\n' + "This is a " + self.type.title() + " restaurant.")

    def status(self): # prints the status of the restaurant
        print(self.name.title() + " is open.")

    def set_num_served(self): # sets how many people the restaurant has served
        self.number_served = 2000
        print("This restaurant has served " + str(self.number_served) + " peoples.")

    def increament_num_served(self, increament): # let increment the num_served
        self.number_served += increament
        print("Number of served incremented by  " + str(self.number_served) + " peoples.")


# creating instance of the class Restaurant
restaurant = Restaurant('Vooter adda', 'chinesse')

print(restaurant.name.title() + " ; type: " + restaurant.type.title() + '\n')

# calling methods
restaurant.describe_res()
restaurant.status()
restaurant.set_num_served()
restaurant.increament_num_served(100)

