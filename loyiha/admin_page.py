import classes


def landing_page(username, password):
    print("Welcome Admin page")
    services = input(f"""
        1. Users
        2. Courses
            >>> """)
    if services == "1":
        classes.User.all_users()
        return landing_page()