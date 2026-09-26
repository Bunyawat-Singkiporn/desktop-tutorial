# 🔐 loop-safety — ข้อ 11: ล็อกอินด้วย while True

**Difficulty:** 🟡 Medium

---

## โจทย์

รหัสถูกต้องคือ `"secret"`
ใช้ `while True` รับรหัส
ถูกรหัสพิมพ์ `Welcome` แล้ว break
ผิดพิมพ์ `Try again` แล้ววนต่อ

---

## Input

รหัสทีละบรรทัดจนถูก

## Output

Try again ตามครั้งที่ผิด แล้ว Welcome

---

## ตัวอย่าง

**Input:**

```text
123
pass
secret
```

**Output:**

```text
Try again
Try again
Welcome
```

---

## 💡 Hint

if/else ใน while True — ถูกแล้ว break

---

## Starter Code

```python
# เขียนโค้ดตรงนี้
```
