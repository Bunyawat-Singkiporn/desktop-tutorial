words = ["hi", "yo", "hi", "hey", "yo", "hi"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
for key, value in count.items():
    print(f"{key}: {value}")
