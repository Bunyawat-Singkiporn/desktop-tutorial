status = ["Present", "Absent", "Present", "Present", "END", "Present"]
count = 0
for s in status:
    if s == "END":
        break
    if s == "Absent":
        continue
    count = count + 1
print(f"Present Count: {count}")
