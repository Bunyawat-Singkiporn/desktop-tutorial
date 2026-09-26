# 🧠 Logic Integration — ข้อ 16: ห้องเรียนสรุปเกรดหยาบ

**Difficulty:** 🔴 Challenge

---

## โจทย์

สรุปสถานะผ่านของทั้งห้อง

**เงื่อนไข:**

- สร้าง `status(score)` คืน `Pass` หรือ `Fail` (เกณฑ์ 50)
- มี `scores = [45, 70, 88]`
- พิมพ์สถานะทีละบรรทัด

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Fail
Pass
Pass
```


---

## 💡 Hint

อย่าทำเกรด A/B/C/F

---

## Starter Code

```python
def status(score):
    # return Pass/Fail

scores = [45, 70, 88]
for s in scores:
    print(status(s))
```
