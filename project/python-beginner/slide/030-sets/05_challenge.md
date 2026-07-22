# 🔥 Practice Sets — Question 4: Class Roster

**Difficulty:** 🔴 Hard

---

## โจทย์

มีชื่อนักเรียนจาก 2 ห้อง (มีชื่อซ้ำข้ามห้อง) แสดง:
1. จำนวนนักเรียนทั้งหมด (ไม่ซ้ำ)
2. ชื่อที่อยู่ในทั้งสองห้อง
3. ชื่อที่อยู่ในห้องใดห้องหนึ่งเท่านั้น (union ลบ intersection)

```python
room_a = ["Alice", "Bob", "Charlie", "Diana"]
room_b = ["Bob", "Eve", "Charlie", "Frank"]
```

**Output** (ลำดับอาจต่างกัน):
```
Total unique students: 6
In both rooms: {'Bob', 'Charlie'}
Only in one room: {'Alice', 'Diana', 'Eve', 'Frank'}
```

---

## 💡 Hint

- แปลง list เป็น set ก่อน
- ใช้ `|` และ `&` และ `-` (difference)

---

## Starter Code

```python
room_a = ["Alice", "Bob", "Charlie", "Diana"]
room_b = ["Bob", "Eve", "Charlie", "Frank"]

set_a = set(room_a)
set_b = set(room_b)

# Write your code here
```
