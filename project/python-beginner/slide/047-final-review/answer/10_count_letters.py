letters = ["a", "b", "a", "c", "a"]
freq = {}
for ch in letters:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq["a"])
