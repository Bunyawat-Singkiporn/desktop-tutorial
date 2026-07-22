# 🔥 Practice Choosing Data Types — Question 4: Best Type

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างโปรแกรมระบบห้องสมุด โดยใช้ชนิดข้อมูลที่เหมาะสม:

| ข้อมูล | ต้องการ | ชนิดที่เหมาะ |
|--------|--------|------------|
| ชื่อหนังสือในคลัง | เพิ่มลบได้, มีลำดับ | List |
| ประเภทหนังสือ | คงที่ไม่เปลี่ยน | Tuple |
| ISBN (ไม่ซ้ำกัน) | ตรวจซ้ำได้รวดเร็ว | Set |

**ต้องทำ:**
1. สร้างข้อมูลตัวอย่างแต่ละชนิด
2. เพิ่มหนังสือใหม่ใน list
3. ตรวจว่า ISBN ใหม่ซ้ำหรือไม่ก่อนเพิ่ม
4. แสดงสรุป

**Output** (ตัวอย่าง):
```
Books: 4
Categories: 3
ISBNs: 4
ISBN-999 is new → added
```

---

## Starter Code

```python
books = ["Python Basics", "Data Science", "Web Dev"]
categories = ("Fiction", "Non-fiction", "Science")
isbns = {"ISBN-001", "ISBN-002", "ISBN-003"}

# เพิ่มหนังสือใหม่ใน books
# ตรวจ ISBN-999 ก่อนเพิ่ม
# แสดงสรุป
```
