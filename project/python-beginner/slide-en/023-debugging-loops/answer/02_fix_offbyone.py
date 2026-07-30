# โจทย์: แก้ Off-by-One — range(1, 10) → range(1, 11)
# Bug: range(1, 10) แสดงแค่ 1–9
# Fix: เปลี่ยนเป็น range(1, 11) เพื่อรวม 10 ด้วย

for i in range(1, 11):   # ✅ แก้แล้ว
    print(i)
