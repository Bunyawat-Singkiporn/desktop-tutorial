# ✨ Code Readability — ข้อ 16: รายงานสะอาด

**Difficulty:** 🔴 Challenge

---

## โจทย์

สร้างรายงานคะแนนให้อ่านง่าย

**เงื่อนไข:**

- `PASS_SCORE = 50`
- สร้าง `is_pass(score)` คืน True/False
- สร้าง `report(name, score)` พิมพ์ `name: Pass` หรือ `name: Fail`
- เรียกกับ `("Yam", 66)` และ `("Bee", 40)`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

2 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Yam: Pass
Bee: Fail
```


---

## 💡 Hint

ใช้ค่าคงที่และฟังก์ชันช่วยอ่าน

---

## Starter Code

```python
PASS_SCORE = 50

def is_pass(score):
    # return เปรียบเทียบ

def report(name, score):
    # พิมพ์ผล

report("Yam", 66)
report("Bee", 40)
```
