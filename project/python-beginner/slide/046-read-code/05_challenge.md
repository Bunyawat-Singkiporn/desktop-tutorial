# 👀 Read Code — ข้อ 5: หาบั๊กในยอดรวม

**Difficulty:** 🔴 Challenge

---

## โจทย์

โค้ดเดิมสะสมผิดเพราะใช้ `total = n` — จงเขียนให้รวม `[5, 5, 5]` ได้ 15

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
15
```


---

## 💡 Hint

ต้องเป็น += ไม่ใช่ =

---

## Starter Code

```python
total = 0
for n in [5, 5, 5]:
    total += n
print(total)
```
