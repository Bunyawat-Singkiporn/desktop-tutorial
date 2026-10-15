words = ["hi", "ok", "hi", "hi"]
freq = {}
for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1
print(freq["hi"])
