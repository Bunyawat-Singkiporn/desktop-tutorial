def is_strong(password):
    if len(password) < 8:
        return False
    for ch in password:
        if ch.isdigit():
            return True
    return False

password = input()
if is_strong(password):
    print("Strong")
else:
    print("Weak")
