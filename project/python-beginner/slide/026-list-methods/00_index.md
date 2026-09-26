# 📋 สารบัญโจทย์ — บท 026 List Methods

**ขอบเขตของบทนี้:** index assign · `.append()` · `.remove()` · `.sort()` / `.sort(reverse=True)` · `print(list)`

> ❌ ไม่มี `.insert()` / `.pop()` / `sorted()` · ไม่มี `in` (บท 030)

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | เพิ่มชื่อเข้ากลุ่มแชท | append ทีละชื่อ |
| 2 | `03_test.md` | 🟢 | แก้ชื่อเมนูผิด | index assignment |
| 3 | `04_test.md` | 🟢 | เอาของหมดสต็อกออก | remove ตามค่า |
| 4 | `08_easy.md` | 🟢 | เรียงราคาน้อยไปมาก | sort ปกติ |
| 5 | `09_easy.md` | 🟢 | เรียงคะแนนมากไปน้อย | sort reverse |
| 6 | `06_medium.md` | 🟡 | อัปเดตรายการซื้อ | append + remove |
| 7 | `07_medium.md` | 🟡 | แก้แล้วเรียงเมนู | index assign + sort |
| 8 | `10_medium.md` | 🟡 | คะแนนหลังตัดทิ้ง | remove + sort reverse |
| 9 | `11_medium.md` | 🟡 | สร้างคิวจากว่าง | append จากว่างหลายครั้ง |
| 10 | `12_medium.md` | 🟡 | แก้ราคาแล้วเรียง | index assign + sort |
| 11 | `13_medium.md` | 🟡 | ลบสองรายการแล้วเรียง | remove สองครั้ง + sort |
| 12 | `05_challenge.md` | 🔴 | จัดการคะแนนสอบ | append+remove+sort |
| 13 | `14_challenge.md` | 🔴 | จัดชั้นวางสินค้า | หลาย method ผสม |
| 14 | `15_challenge.md` | 🔴 | คิวหน้าร้านกาแฟ | append+remove+กล่อง |
| 15 | `16_challenge.md` | 🔴 | กระดานคะแนนเกม | ครบทุก method + สรุป |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ 02 ไม่ซ้ำตัวอย่าง fruits/scores ในบทเรียนแบบเดิมทุกขั้น
- ใช้ได้เฉพาะ append / remove / sort / index assign
- ห้าม insert / pop / sorted / in
