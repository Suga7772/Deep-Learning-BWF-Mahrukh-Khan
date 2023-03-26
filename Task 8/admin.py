from user import User


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges([])  # initialising empty set for future storing


class Privileges():
    def __init__(self, privileges):
        self.privilege = privileges

    def show_priv(self):
        for p in self.privileges:
            print(p)
