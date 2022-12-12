class Users(): # creating a class

    def __init__(self, f_name, l_name, username, age): # initialize atributes to describe user
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.age = age
        self.login_atempt = 0

    def describe_user(self): # creating a method to describe the user
        print("User Description: ")
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

user1  = Users('Arafat', 'Islam', 'Thorfast Hawk', 20) # creating a instance of the class

user1.describe_user() # calling describe method to describe user
user1.greet_user() # calling greet method to greet the user
print('\n')

for attempt in range(0,5): # using a for loop to increment the atttempt number
    user1.increment_login_atempts()
print('\n')

user1.resets_login_atempt() # calling reset method to reset the login attempt value

