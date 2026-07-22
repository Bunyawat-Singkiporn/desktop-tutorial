# โจทย์: หา word ที่ยาวที่สุดใน list

words = ["cat", "elephant", "dog", "butterfly", "ox"]
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print(f"Longest: {longest} ({len(longest)})")
