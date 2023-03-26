class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location)

    def greet_user(self):
        print("\nWelcome " + self.username + "<3")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self): #reset to 0
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


class Privileges():
    def __init__(self, privileges):
        self.privilege = privileges

    def show_priv(self):
        for p in self.privileges:
            print(p)