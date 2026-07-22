# result เท่ากับ: 10 (2 + 8 = 10 — เฉพาะเลขคู่)
# Output คือ: 10

numbers = [2, 5, 3, 8, 1]
result = 0

for n in numbers:
    if n % 2 == 0:
        result += n

print(result)
