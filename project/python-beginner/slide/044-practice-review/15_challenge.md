# 🔁 Practice Review — ข้อ 15: จัดทีมไม่ซ้ำ

**Difficulty:** 🔴 Challenge

---

## โจทย์

รายชื่อสมัครอาจซ้ำ ให้เหลือชื่อไม่ซ้ำแล้วเรียงด้วย .sort()

**เงื่อนไข:**

- จาก `raw = ["C", "A", "B", "A"]`
- สร้าง list ใหม่โดยเพิ่มเฉพาะชื่อที่ยังไม่มี แล้ว sort
- พิมพ์ list ผลลัพธ์

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
['A', 'B', 'C']
```


---

## 💡 Hint

ใช้ in กับ list แล้ว sort

---

## Starter Code

```python
raw = ["C", "A", "B", "A"]
team = []
for name in raw:
    # เพิ่มถ้ายังไม่มี
team.sort()
print(team)
```
