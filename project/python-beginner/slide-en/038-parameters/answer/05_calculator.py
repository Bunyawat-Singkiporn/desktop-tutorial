def calculate(a, b, op):
    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        if b == 0:
            print(f"{a} / {b} = Cannot divide by zero")
        else:
            print(f"{a} / {b} = {a / b}")

calculate(3, 5, "+")
calculate(10, 4, "-")
calculate(6, 7, "*")
calculate(10, 2, "/")
calculate(10, 0, "/")
