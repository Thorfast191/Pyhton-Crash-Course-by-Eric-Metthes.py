class Users(): # creating a class

    def __init__(self, f_name, l_name, username, age): # initialize atributes to describe user
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.age = age

    def describe_user(self): # creating a method to describe the user
        print("User Description: ")
        print("First name: " + self.f_name + '\n'
              + "Last name: " + self.l_name + '\n'
              + "Username: " + self.username + '\n'
              + "Age: " + f'{self.age}' + '\n')

    def greet_user(self): # creating a method to greet user
        full_name = self.f_name + ' ' + self.l_name
        print("Hey, what's up "+ full_name + ". Have a greate day.")

user1  = Users('Arafat', 'Islam', 'Thorfast Hawk', 20) # creating a instance of the class

user1.describe_user() # calling the methods by instance
user1.greet_user()

