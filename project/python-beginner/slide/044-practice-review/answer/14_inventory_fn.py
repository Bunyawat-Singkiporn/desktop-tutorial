def add_stock(inv, item, n):
    if item in inv:
        inv[item] = inv[item] + n
    else:
        inv[item] = n

inv = {}
add_stock(inv, "apple", 3)
add_stock(inv, "apple", 3)
print(inv)
