# 🎯 loop-safety — ข้อ 5: ทายเลขพร้อมคำใบ้

**Difficulty:** 🔴 Challenge

---

## โจทย์

เลขลับคือ `25`
ใช้ `while True` รับคำทาย
- ถูก → พิมพ์ `Correct!` แล้ว break
- น้อยเกินไป → พิมพ์ `Too low` แล้ว continue
- มากเกินไป → พิมพ์ `Too high` แล้ว continue

---

## Input

คำทายทีละบรรทัด

## Output

คำใบ้จนถูก

---

## ตัวอย่าง

**Input:**

```text
10
40
25
```

**Output:**

```text
Too low
Too high
Correct!
```

---

## 💡 Hint

เทียบ guess กับ secret ด้วย if / elif / else ใน while True

---

## Starter Code

```python
secret = 25

# เขียนโค้ดตรงนี้
```
