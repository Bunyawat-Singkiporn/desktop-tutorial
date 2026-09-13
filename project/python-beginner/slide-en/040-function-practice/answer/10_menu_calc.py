def add(a, b):
    return a + b

def mul(a, b):
    return a * b

a = int(input())
b = int(input())
choice = input()

if choice == "1":
    print(f"Result: {add(a, b)}")
elif choice == "2":
    print(f"Result: {mul(a, b)}")
else:
    print("Invalid")
