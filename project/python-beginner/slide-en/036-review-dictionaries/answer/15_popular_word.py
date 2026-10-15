words = ["go", "run", "go", "jump", "go", "run"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
top_word = ""
top_n = 0
for word, n in count.items():
    if n > top_n:
        top_n = n
        top_word = word
print(f"Popular: {top_word} ({top_n})")
