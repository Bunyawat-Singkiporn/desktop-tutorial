# ⏭️ Practice: Loop Safety — Question 2: Skip Even Numbers

**Difficulty:** 🟡 Medium

---

## โจทย์

วนซ้ำ 1–10 แต่ข้ามเลขคู่ทั้งหมด แสดงเฉพาะเลขคี่

**Output:**
```
1
3
5
7
9
```

---

## 💡 Hint

- ถ้า `i % 2 == 0` (เลขคู่) ให้ `continue`
- ถ้าไม่ใช่ก็ `print` ปกติ

---

## Starter Code

```python
for i in range(1, 11):
    if i % 2 == 0:
        # Skip even numbers
    print(i)
```
