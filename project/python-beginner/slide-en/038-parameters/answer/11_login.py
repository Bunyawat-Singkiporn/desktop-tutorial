def login(user, password):
    if user == "admin" and password == "1234":
        print("Access granted")
    else:
        print("Access denied")

user = input()
password = input()
login(user, password)
