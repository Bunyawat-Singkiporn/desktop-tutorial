# 🏁 Final Review — ข้อ 14: รายงานห้องเรียน

**Difficulty:** 🔴 Challenge

---

## โจทย์

dict ของ list คะแนน พิมพ์ชื่อกับผลรวม

**เงื่อนไข:**

- `room = {"A": [10, 20], "B": [30, 5]}`
- พิมพ์ `A: 30` และ `B: 35`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

2 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
A: 30
B: 35
```


---

## 💡 Hint

dict of lists

---

## Starter Code

```python
room = {"A": [10, 20], "B": [30, 5]}
for name, scores in room.items():
    print(f"{name}: {sum(scores)}")
```
