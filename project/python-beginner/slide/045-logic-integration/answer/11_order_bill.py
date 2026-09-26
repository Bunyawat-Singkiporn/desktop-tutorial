menu = {"a": 40, "b": 25}
order = ["a", "b", "a"]
total = 0
for item in order:
    total += menu[item]
print(total)
