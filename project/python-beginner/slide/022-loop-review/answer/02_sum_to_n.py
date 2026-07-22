# โจทย์: รวมตัวเลข 1 ถึง n

n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i

print(f"Sum from 1 to {n} = {total}")
