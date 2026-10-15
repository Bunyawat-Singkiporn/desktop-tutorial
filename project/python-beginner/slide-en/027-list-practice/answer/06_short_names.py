names = ["Ann", "Bobby", "Cy", "Diana", "Ed"]
short = []
for name in names:
    if len(name) <= 3:
        short.append(name)
print(short)
