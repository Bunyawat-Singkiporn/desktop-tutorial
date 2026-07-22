# ข้อ 9 : nested loop
# โจทย์: รับตัวเลข n แล้วแสดงตารางสูตรคูณขนาด n x n

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()
