import login
import register

def main():
    web = input("""
        1. Login
        2. Register
            >>> """)

    if web == "1":
        return login.login()

    elif web == "2":
         return register.register()

    else:
        print("Error!")
        return main()

if __name__ == "__main__":
    main()