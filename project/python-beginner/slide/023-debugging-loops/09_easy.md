# 🐛 debugging-loops — ข้อ 9: แก้ range คู่

**Difficulty:** 🟢 Easy

---

## โจทย์

ต้องการพิมพ์เลขคู่ `2 4 6 8 10` แต่ตอนนี้หยุดที่ `8`
แก้ค่า stop ของ `range`

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

เลขคู่ 2 ถึง 10

---

## ตัวอย่าง

**Output:**

```text
2
4
6
8
10
```


---

## 💡 Hint

ต้องตั้ง stop ให้เลยค่าสุดท้ายที่ต้องการ

---

## Starter Code

```python
for i in range(2, 10, 2):  # ← แก้
    print(i)
```
