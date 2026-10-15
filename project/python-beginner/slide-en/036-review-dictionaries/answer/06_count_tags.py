tags = ["fun", "code", "fun", "game", "code", "fun"]
count = {}
for tag in tags:
    if tag in count:
        count[tag] += 1
    else:
        count[tag] = 1
for key, value in count.items():
    print(f"{key}: {value}")
