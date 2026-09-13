basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
count = {}

for fruit in basket:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

for fruit, n in count.items():
    print(f"{fruit}: {n}")
