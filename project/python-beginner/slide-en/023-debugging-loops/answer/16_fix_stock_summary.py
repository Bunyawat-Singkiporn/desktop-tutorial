stock = [4, 0, 7, 0, 3]
shelves = 0
items = 0
for qty in stock:
    if qty == 0:
        continue
    shelves = shelves + 1
    items = items + qty
print(f"Shelves: {shelves}")
print(f"Items: {items}")
