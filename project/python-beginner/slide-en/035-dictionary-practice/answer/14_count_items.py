items = ["pen", "book", "pen", "glue", "book", "pen"]
count = {}
for item in items:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
keys = list(count)
keys.sort()
for key in keys:
    print(f"{key}: {count[key]}")
