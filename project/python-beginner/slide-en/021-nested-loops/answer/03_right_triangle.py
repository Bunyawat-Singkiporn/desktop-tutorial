# โจทย์: แสดงสามเหลี่ยมมุมฉากตามขนาดที่รับ

n = int(input())

# loop นอก: แถว 1 ถึง n
for row in range(1, n + 1):
    # loop ใน: วน row ครั้ง (เพิ่มขึ้นทุกแถว)
    for col in range(row):
        print("*", end="")
    print()   # ขึ้นบรรทัดใหม่
