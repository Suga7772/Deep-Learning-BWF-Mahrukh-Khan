# login attempts

class User():
    def __init__(self, fname, lname, uname, email, loc):
        # attribute initialisation
        self.first_name = fname.title()
        self.last_name = lname.title()
        self.username = uname
        self.email = email
        self.location = loc.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back " + self.username + "<3")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self): #reset to 0
        self.login_attempts = 0


vix = User('Vix', 'Xen', 'V-ixen', 'Vixen@example.com', 'Ottawa')
vix.describe_user()
vix.greet_user()

print("\nMaking 4 login attempts...")
vix.increment_login_attempts()
vix.increment_login_attempts()
vix.increment_login_attempts()
vix.increment_login_attempts()
print("  Login attempts are " + str(vix.login_attempts))
print("Resetting the login attempts")
vix.reset_login_attempts()
print("  Login attempts: " + str(vix.login_attempts))