names = ["Ann", "Ben", "Cara", "Dan"]
target = input()
pos = 1
result = "Not Found"
for name in names:
    if name == target:
        result = f"Found at {pos}"
        break
    pos = pos + 1
print(result)
