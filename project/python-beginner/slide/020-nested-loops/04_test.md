# ✖️ Practice: Nested Loops — Question 3: Multiplication Table

**Difficulty:** 🟡 Medium

---

## โจทย์

รับจำนวน n แล้วแสดงตารางสูตรคูณ n×n

**Input:**
```
4
```

**Output:**
```
1  2  3  4  
2  4  6  8  
3  6  9  12  
4  8  12  16  
```

---

## 💡 Hint

- Loop นอก: แถว 1–n
- Loop ใน: คอลัมน์ 1–n
- `print(i * j, end="  ")` พิมพ์ตัวเลขและ space

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Print i * j with spaces
    # Move to next line
```
