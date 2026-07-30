prices = {"apple": 15, "banana": 8, "mango": 25, "orange": 20, "kiwi": 35}
total = 0

for i in range(3):
    item = input(f"Item {i+1}: ")
    if item in prices:
        print(f"{item}: {prices[item]}")
        total += prices[item]
    else:
        print(f"Not found: {item}")

print(f"Total: {total} บาท")
