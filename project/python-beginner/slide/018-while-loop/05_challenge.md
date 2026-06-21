# 🔥 Practice: while Loop — Question 4: Number Accumulator

**Difficulty:** 🔴 Hard

---

## โจทย์

รับตัวเลขซ้ำๆ จนกว่าผู้ใช้จะพิมพ์ `0` แล้วแสดงสถิติ

**Input:**
```
5
12
3
8
0
```

**Output:**
```
Count: 4
Total: 28
Average: 7.00
Largest: 12
Smallest: 3
```

---

## 💡 Hint

- ใช้ `while True:` + `break` เมื่อรับ 0
- เก็บตัวเลขทุกตัวใน list
- ใช้ `max()`, `min()`, `sum()`, `len()` คำนวณ

---

## Starter Code

```python
numbers = []

while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(n)

# Calculate and print stats
```
