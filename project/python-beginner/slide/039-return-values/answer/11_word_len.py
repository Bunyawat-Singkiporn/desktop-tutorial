def name_length(text):
    return len(text)

def can_register(text):
    return name_length(text) >= 8

username = input()
print(f"Username: {username}")
print(f"Length: {name_length(username)}")
if can_register(username):
    print("Status: OK to register")
else:
    print("Status: Too short")
