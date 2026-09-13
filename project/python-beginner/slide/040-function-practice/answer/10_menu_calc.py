def add(a, b):
    return a + b

def mul(a, b):
    return a * b

a = int(input())
b = int(input())
choice = input()
print("Calculator")
if choice == "1":
    print(f"{a} + {b} = {add(a, b)}")
elif choice == "2":
    print(f"{a} * {b} = {mul(a, b)}")
else:
    print("Unknown button")
