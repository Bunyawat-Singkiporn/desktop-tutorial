n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        count = count + 1
print(f"Special Boxes: {count}")
