# 🐛 debugging-loops — ข้อ 6: แก้รวมยอดใน list

**Difficulty:** 🟡 Medium

---

## โจทย์

ต้องการรวมราคา `[25, 40, 15]` แต่เขียน `total = price` ทำให้เหลือแค่ราคาสุดท้าย

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

บรรทัดเดียว Total

---

## ตัวอย่าง

**Output:**

```text
Total: 80
```


---

## 💡 Hint

ต้องบวกเข้า total เดิม ไม่ใช่แทนที่

---

## Starter Code

```python
prices = [25, 40, 15]
total = 0
for price in prices:
    total = price  # ← แก้
print(f"Total: {total}")
```
