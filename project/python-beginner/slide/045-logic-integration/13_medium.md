# 🧠 Logic Integration — ข้อ 13: สรุปผ่าน/ตก

**Difficulty:** 🟡 Medium

---

## โจทย์

นับจำนวนผ่านและตก

**เงื่อนไข:**

- `scores = [40, 60, 55, 30, 80]` เกณฑ์ 50
- พิมพ์ `Pass: x` และ `Fail: y`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

2 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Pass: 3
Fail: 2
```


---

## 💡 Hint

นับสองตัวแปร

---

## Starter Code

```python
scores = [40, 60, 55, 30, 80]
passed = 0
failed = 0
for s in scores:
    # นับ
print(f"Pass: {passed}")
print(f"Fail: {failed}")
```
