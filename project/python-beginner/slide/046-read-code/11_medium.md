# 👀 Read Code — ข้อ 11: นับรอบที่เข้าเงื่อนไข

**Difficulty:** 🟡 Medium

---

## โจทย์

นับว่ามีกี่ตัวใน `[1, 4, 6, 3]` ที่มากกว่า 3

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
2
```


---

## 💡 Hint

นับเมื่อเงื่อนไขเป็นจริง

---

## Starter Code

```python
nums = [1, 4, 6, 3]
count = 0
for n in nums:
    if n > 3:
        count += 1
print(count)
```
