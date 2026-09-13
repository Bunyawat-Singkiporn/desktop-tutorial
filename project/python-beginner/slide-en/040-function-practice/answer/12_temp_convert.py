def to_f(c):
    return c * 9 / 5 + 32

def to_c(f):
    return (f - 32) * 5 / 9

mode = input()
value = float(input())
print("Travel Helper")
if mode == "C":
    print(f"{value} C = {to_f(value):.2f} F")
elif mode == "F":
    print(f"{value} F = {to_c(value):.2f} C")
else:
    print("Unknown mode")
