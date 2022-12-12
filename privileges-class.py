class Users(): # creating a class

    def __init__(self, f_name, l_name, username, age): # initialize atributes to describe user
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.age = age
        self.login_atempt = 0

    def describe_user(self): # creating a method to describe the user
        print("Description: ")
        print("First name: " + self.f_name + '\n'
              + "Last name: " + self.l_name + '\n'
              + "Username: " + self.username + '\n'
              + "Age: " + f'{self.age}' + '\n')

    def greet_user(self): # creating a method to greet user
        full_name = self.f_name + ' ' + self.l_name
        print("Hey, what's up "+ full_name + ". Have a greate day.")

    def increment_login_atempts(self): # let us increament login atempt
        self.login_atempt += 1
        print("login atempt incremented by " + str(self.login_atempt)) # prints login attempt

    def resets_login_atempt(self): # let us reset the atempt value

        if self.login_atempt > 0: # logic to reset the value
            self.login_atempt = 0

            print("Login attempts have been reseted to " + str(self.login_atempt)) # prints reset value

        else: print("Login attempts is already  " + str(self.login_atempt))

class Admin(Users):
    def __init__(self, f_name, l_name, username, age):
        super().__init__(f_name, l_name, username, age) # connecting child_class with super_class
        self.privileges = Privileges()


class Privileges(Admin):
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:  # looping through privileges to print privilege
                print("Admin can " + privilege)

user1  = Users('Arafat', 'Islam', 'Thorfast Hawk', 20) # creating a instance of the class
admin = Admin('Arafat', 'Islam', 'Thorfast Hawk', 20) # creating an instance of the child_class

admin_privileges = ['can add user', 'can ban users'] # storing data

user1.describe_user() # calling describe method to describe user
user1.greet_user() # calling greet method to greet the user
admin.privileges.show_privileges()

print("\nAdding privileges...")
privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = privileges
admin.privileges.show_privileges()
print('\n')

for attempt in range(0,5): # using a for loop to increment the attempt number
    user1.increment_login_atempts()
print('\n')

user1.resets_login_atempt() # calling reset method to reset the login attempt value

