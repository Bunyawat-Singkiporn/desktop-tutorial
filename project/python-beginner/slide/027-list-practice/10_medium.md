# 🏋️ List Practice — ข้อ 10: รายการงานพร้อมสถานะ

**Difficulty:** 🟡 Medium

---

## โจทย์

แอปงานบ้านทำเครื่องหมาย Done ให้งานข้อคู่ (index คู่)

กำหนด `tasks = ["Sweep", "Mop", "Dust", "Wipe"]`

ใช้ range(len) แสดง `0 Sweep Done` หรือ `1 Mop Todo` ตามว่า index หาร 2 ลงตัวหรือไม่

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

4 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
0 Sweep Done
1 Mop Todo
2 Dust Done
3 Wipe Todo
```


---

## 💡 Hint

ใช้ i % 2 == 0 แยกสถานะ

---

## Starter Code

```python
tasks = ["Sweep", "Mop", "Dust", "Wipe"]

# เขียนโค้ดตรงนี้
```
