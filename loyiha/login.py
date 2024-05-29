from classes import User

def login():
    print("Login Page")
    username = input("Username: ")
    password = input("Password: ")
    if User.check_user(username, password) is False:
        return login()