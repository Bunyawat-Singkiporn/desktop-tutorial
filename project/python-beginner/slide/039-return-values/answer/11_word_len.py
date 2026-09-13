def word_len(text):
    return len(text)

def is_long(text):
    return word_len(text) >= 8

text = input()
print(f"Length: {word_len(text)}")
if is_long(text):
    print("Long")
else:
    print("Short")
