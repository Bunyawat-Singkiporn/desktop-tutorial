# โจทย์: แสดงสี่เหลี่ยมผืนผ้าขนาด 4×3

# loop นอก: 3 แถว
for row in range(3):
    # loop ใน: 4 ดาวต่อแถว
    for col in range(4):
        print("*", end="")
    print()   # ขึ้นบรรทัดใหม่หลังจบแถว
