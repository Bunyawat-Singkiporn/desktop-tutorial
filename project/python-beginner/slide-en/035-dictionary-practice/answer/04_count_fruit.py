fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
count = {}
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
for key, value in count.items():
    print(f"{key}: {value}")
