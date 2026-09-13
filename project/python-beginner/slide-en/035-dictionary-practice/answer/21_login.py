accounts = {"alice": "1234", "bob": "abcd"}

user = input()
password = input()
if user in accounts and accounts[user] == password:
    print("Welcome!")
else:
    print("Login failed")
