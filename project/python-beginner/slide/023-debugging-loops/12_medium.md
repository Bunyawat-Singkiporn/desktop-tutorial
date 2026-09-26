# 🐛 debugging-loops — ข้อ 12: แก้ break เร็วเกิน

**Difficulty:** 🟡 Medium

---

## โจทย์

พิมพ์คิว `["Wait", "Wait", "Serve", "Wait"]` จนเจอ `Serve` รวมการพิมพ์ Serve ด้วย

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

Wait Wait Serve

---

## ตัวอย่าง

**Output:**

```text
Wait
Wait
Serve
```


---

## 💡 Hint

พิมพ์ก่อน แล้วค่อย break

---

## Starter Code

```python
queue = ["Wait", "Wait", "Serve", "Wait"]
for item in queue:
    if item == "Serve":
        break
    print(item)
```
