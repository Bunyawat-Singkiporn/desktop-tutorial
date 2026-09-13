def show_max(a, b):
    if a > b:
        print(f"Max: {a}")
    elif b > a:
        print(f"Max: {b}")
    else:
        print("Equal")

a = int(input())
b = int(input())
show_max(a, b)
