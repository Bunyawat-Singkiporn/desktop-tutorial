def field_area(width, length):
    return width * length

width = float(input())
length = float(input())
area = field_area(width, length)
print("Football Field")
print(f"Width: {width}")
print(f"Length: {length}")
print(f"Area: {area}")
