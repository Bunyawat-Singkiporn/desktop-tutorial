# 🔁 Practice Review — ข้อ 11: นับความถี่คำสั้น

**Difficulty:** 🟡 Medium

---

## โจทย์

นับคำใน list

**เงื่อนไข:**

- จาก `words = ["hi", "ok", "hi", "hi"]` สร้าง dict นับความถี่
- พิมพ์ค่าของคีย์ `"hi"`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
3
```


---

## 💡 Hint

แบบนับความถี่ด้วย dict

---

## Starter Code

```python
words = ["hi", "ok", "hi", "hi"]
freq = {}
for w in words:
    # นับใน dict
print(freq["hi"])
```
