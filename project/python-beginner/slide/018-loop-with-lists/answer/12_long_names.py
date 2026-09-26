names = ["Ann", "Bobby", "Chris", "Di", "Elena"]
count = 0
for name in names:
    if len(name) > 4:
        count = count + 1
print(f"Long Names: {count}")
