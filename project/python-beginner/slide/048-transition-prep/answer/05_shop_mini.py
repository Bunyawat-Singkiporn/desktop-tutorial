menu = {"bun": 25, "milk": 20}
order = ["bun", "milk", "bun"]
total = 0
for item in order:
    total += menu[item]
print(total)
