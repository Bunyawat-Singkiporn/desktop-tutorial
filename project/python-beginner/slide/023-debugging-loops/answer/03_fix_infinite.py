# โจทย์: แก้ Infinite Loop — เพิ่ม count = count + 1
# Bug: ลืม count = count + 1 ทำให้วนไม่หยุด

count = 1
while count <= 5:
    print(count)
    count = count + 1   # ✅ แก้แล้ว — ต้องมีบรรทัดนี้
