def to_fahrenheit(c):
    return c * 9 / 5 + 32

c = float(input())
f = to_fahrenheit(c)
print("Trip Weather")
print(f"{c} C = {f} F")
