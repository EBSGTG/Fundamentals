import re


def logining():
    print("Please enter your credentials")
    login = input()
    password = input()
    return login, password


def validation(login, password):
    needed_phrase = "@gmail.com"
    if login and password:
        if needed_phrase not in login:
            print("Your login is invalid! Try again")
            login, password = logining()
            validation(login, password)
        finder = re.search(r'^[A-Z].*\d.*$', password)
        if not finder:
            print("Your password is invalid! Try again")
            login, password = logining()
            validation(login, password)
    else:
        print("Enter your credentials")

    print("Welcome to Cum")

