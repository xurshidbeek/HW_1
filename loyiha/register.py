from classes import User
import login

def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    user = User(first_name, last_name, username, password)
    user.save()
    return login.login()

