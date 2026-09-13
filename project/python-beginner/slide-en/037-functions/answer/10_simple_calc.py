def simple_calc():
    a = float(input())
    b = float(input())
    op = input()
    if op == "+":
        print(a + b)
    elif op == "*":
        print(a * b)
    else:
        print("Unknown")

simple_calc()
