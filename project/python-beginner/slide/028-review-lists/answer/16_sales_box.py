sales = [900, 1200, 750, 1100]
sales.remove(750)
sales.append(1300)
sales.sort()
total = 0
for s in sales:
    total += s
print("====================")
print(sales)
print(f"Total  : {total}")
print(f"Highest: {sales[-1]}")
print("====================")
