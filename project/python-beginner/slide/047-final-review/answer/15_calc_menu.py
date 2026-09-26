def add(a, b):
    return a + b

def mul(a, b):
    return a * b

op = int(input())
a = int(input())
b = int(input())
if op == 1:
    print(add(a, b))
else:
    print(mul(a, b))
