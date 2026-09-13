prices = {"pen": 10, "book": 40, "eraser": 5, "ruler": 15}
total = 0

for i in range(2):
    item = input(f"Item {i+1}: ")
    if item in prices:
        total += prices[item]

print(f"Total: {total} baht")
