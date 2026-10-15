total = 0
while True:
    text = input()
    if text == "done":
        break
    total += int(text)
print(f"Total: {total}")
