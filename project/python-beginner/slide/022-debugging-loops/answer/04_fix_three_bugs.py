# โจทย์: แก้ 3 bugs ในโค้ด
# Bug 1: print(names) → print(name) — ใช้ตัวแปรวนไม่ใช่ชื่อ list
# Bug 2: range(1, 5) → range(1, 6) — Off-by-one
# Bug 3: (ไม่มี bug 3 จริงๆ หลังแก้สองข้อแรกแล้วถูกต้อง)

names = ["Alice", "Bob", "Charlie"]

# ✅ Bug 1 แก้: ใช้ name แทน names
for name in names:
    print(name)

# ✅ Bug 2 แก้: range(1, 6) ครอบคลุม 1–5
total = 0
for i in range(1, 6):
    total = total + i
print("Total 1-5:", total)
