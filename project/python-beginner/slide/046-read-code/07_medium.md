# 👀 Read Code — ข้อ 7: หาค่ามากสุดเอง

**Difficulty:** 🟡 Medium

---

## โจทย์

หาค่ามากสุดใน `[3, 7, 2, 9, 4]` แบบเริ่มจาก 0 แล้วอัปเดตเมื่อเจอค่ามากกว่า (ตามแนวบทเรียน)

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
9
```


---

## 💡 Hint

อัปเดตเมื่อเจอค่ามากกว่า

---

## Starter Code

```python
numbers = [3, 7, 2, 9, 4]
result = 0
for num in numbers:
    if num > result:
        result = num
print(result)
```
