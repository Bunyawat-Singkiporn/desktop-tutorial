# 🐛 debugging-loops — ข้อ 10: แก้ข้ามเลขศูนย์

**Difficulty:** 🟡 Medium

---

## โจทย์

พิมพ์เลขใน list `[3, 0, 5, 0, 2]` แต่ข้ามศูนย์
`continue` อยู่หลัง `print` — จัดลำดับใหม่

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

เลขที่ไม่ใช่ศูนย์

---

## ตัวอย่าง

**Output:**

```text
3
5
2
```


---

## 💡 Hint

ต้องตัดสินใจข้ามก่อนพิมพ์

---

## Starter Code

```python
nums = [3, 0, 5, 0, 2]
for n in nums:
    print(n)
    if n == 0:
        continue
```
