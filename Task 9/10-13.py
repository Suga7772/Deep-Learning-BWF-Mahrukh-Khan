# 10-13
# this program will iniitlaising upon first run give file erro as no data or stream is inputted
# but upon running prgram second time you will be asked if you are the same user as previously mentioned
# da power of JSON  filesss

import json

def get_stored_username():
    filename = 'user.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        print("File 404 error")
    else:
        return username


def get_new_username():
    username = input("Enter your name ")
    filename = 'user.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (yes or no) ")
        if correct == 'yes':
            print("Welcome back, " + username + " <3")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + " <3")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + " <3")

# invoking the function
greet_user()
