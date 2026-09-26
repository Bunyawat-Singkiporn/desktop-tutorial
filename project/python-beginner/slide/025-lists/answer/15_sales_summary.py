sales = [1200, 980, 1500, 1100]
total = 0
highest = sales[0]
for s in sales:
    total += s
    if s > highest:
        highest = s
average = total / len(sales)
print(f"Total  : {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
