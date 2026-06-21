# 🔥 Practice: Loop Safety — Question 4: Number Filter

**Difficulty:** 🔴 Hard

---

## โจทย์

รับตัวเลขซ้ำๆ จนพิมพ์ `0` โดยแสดงเฉพาะเลขที่ **หารด้วย 3 ลงตัว** และนับจำนวน

**Input:**
```
3
7
9
2
12
5
6
0
```

**Output:**
```
3
9
12
6
Count of multiples of 3: 4
```

---

## 💡 Hint

- `while True:` + `break` เมื่อรับ 0
- ถ้า `n % 3 != 0` ให้ `continue` (ข้าม)
- ถ้า `n % 3 == 0` ให้ print และเพิ่ม count

---

## Starter Code

```python
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 3 != 0:
        continue   # Skip non-multiples
    # Print and count multiples of 3

print(f"Count of multiples of 3: {count}")
```
