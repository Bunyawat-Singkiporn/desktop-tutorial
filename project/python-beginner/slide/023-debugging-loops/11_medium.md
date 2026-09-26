# 🐛 debugging-loops — ข้อ 11: แก้ตารางดาว

**Difficulty:** 🟡 Medium

---

## โจทย์

ต้องการตารางดาว 2 แถว ละ 4 ดอก แต่ลูปในใช้ `range(row)`

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

สองแถวดาวละ 4

---

## ตัวอย่าง

**Output:**

```text
****
****
```


---

## 💡 Hint

ความกว้างคงที่ ไม่ผูกกับหมายเลขแถว

---

## Starter Code

```python
for row in range(2):
    for col in range(row):  # ← แก้
        print("*", end="")
    print()
```
