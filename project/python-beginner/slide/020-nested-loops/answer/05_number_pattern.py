# โจทย์: แสดง pattern ตัวเลข 1 2 3 ... ตามจำนวนแถว

n = int(input())

# loop นอก: แถว 1 ถึง n
for row in range(1, n + 1):
    # loop ใน: ตัวเลข 1 ถึง row
    for j in range(1, row + 1):
        print(j, end=" ")
    print()   # ขึ้นบรรทัดใหม่
