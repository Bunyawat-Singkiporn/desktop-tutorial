# 🧩 Function Practice — ข้อ 5: ระบบคะแนน dict

**Difficulty:** 🔴 Challenge

---

## โจทย์

เก็บคะแนนนักเรียนใน dict

**เงื่อนไข:**

- `add_score(scores, name, score)` ใส่คะแนนแล้วคืน scores
- `get_average(scores)` คืนค่าเฉลี่ยจาก `.values()`
- เพิ่ม Alice=80 Bob=100 แล้วพิมพ์ค่าเฉลี่ย

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
90.0
```


---

## 💡 Hint

ใช้ .values() รวมคะแนน

---

## Starter Code

```python
def add_score(scores, name, score):
    # เขียนโค้ดตรงนี้

def get_average(scores):
    # เขียนโค้ดตรงนี้

scores = {}
scores = add_score(scores, "Alice", 80)
scores = add_score(scores, "Bob", 100)
print(get_average(scores))
```
