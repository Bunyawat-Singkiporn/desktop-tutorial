def login(user, password):
    if user == "player1" and password == "abc123":
        print("Login success! Let's play")
    else:
        print("Login failed")

user = input()
password = input()
login(user, password)
