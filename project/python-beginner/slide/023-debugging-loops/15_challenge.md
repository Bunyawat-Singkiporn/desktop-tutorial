# 🐛 debugging-loops — ข้อ 15: แก้ผังที่นั่ง

**Difficulty:** 🔴 Challenge

---

## โจทย์

ต้องการผัง 2 แถว ละ 3 ที่แบบ `R1: 1 2 3` และ `R2: 1 2 3`
โค้ดเริ่มต้นใช้หมายเลขแถวผิดและลูปในสั้นเกิน — แก้ให้ถูก

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

สองบรรทัดผังที่นั่ง

---

## ตัวอย่าง

**Output:**

```text
R1: 1 2 3 
R2: 1 2 3 
```


---

## 💡 Hint

แถวและที่นั่งควรเริ่มที่ 1 และที่นั่งมี 3 ช่อง

---

## Starter Code

```python
for row in range(2):
    print(f"R{row}:", end=" ")
    for seat in range(2):
        print(seat, end=" ")
    print()
```
