height = 5
width = 7
for row in range(height):
    for col in range(width):
        if row == 0 or row == height - 1 or col == 0 or col == width - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
