# 🐛 debugging-loops — ข้อ 7: แก้ while ทายรหัส

**Difficulty:** 🟡 Medium

---

## โจทย์

รหัสลับคือ `7` รับเดาจนกว่าจะถูกแล้วพิมพ์ `Unlocked`
เงื่อนไข while กลับด้าน — แก้ให้ถูก

---

## Input

ตัวเลขทายทีละบรรทัด จนตรงรหัส

## Output

Unlocked เมื่อเดาถูก

---

## ตัวอย่าง

**Input:**

```text
3
7
```

**Output:**

```text
Unlocked
```


---

## 💡 Hint

วนซ้ำขณะที่ยังเดาไม่ถูก

---

## Starter Code

```python
secret = 7
guess = int(input())
while guess == secret:  # ← แก้เงื่อนไข
    guess = int(input())
print("Unlocked")
```
