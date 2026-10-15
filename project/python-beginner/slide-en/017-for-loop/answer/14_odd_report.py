n = int(input())
count = 0
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        count = count + 1
        total = total + i
print("========================")
print("      ODD REPORT")
print("========================")
print(f"Count : {count}")
print(f"Sum   : {total}")
print("========================")
