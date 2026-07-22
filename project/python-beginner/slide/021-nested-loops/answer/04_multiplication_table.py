# โจทย์: แสดงตารางสูตรคูณ n×n

n = int(input())

# loop นอก: แถว (ตัวคูณแรก)
for i in range(1, n + 1):
    # loop ใน: คอลัมน์ (ตัวคูณสอง)
    for j in range(1, n + 1):
        print(i * j, end="  ")   # พิมพ์ผลคูณและ space
    print()   # ขึ้นบรรทัดใหม่หลังแต่ละแถว
