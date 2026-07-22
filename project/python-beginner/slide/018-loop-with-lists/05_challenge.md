# 🔥 Practice: Loop with Lists — Question 4: List Printer with Stats

**Difficulty:** 🔴 Hard

---

## โจทย์

วนซ้ำ list ตัวเลขด้านล่าง แล้วแสดงผลลัพธ์ครบทุกอย่าง

```python
numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]
```

**Output:**
```
Numbers: 3 7 1 9 4 6 2 8 5
Count: 9
Total: 45
Max: 9
Min: 1
Average: 5.0
```

---

## 💡 Hint

- พิมพ์ทุกตัวในบรรทัดเดียวด้วย `print(n, end=" ")`
- ใช้ `max()`, `min()`, `len()`, `sum()` ได้เลย

---

## Starter Code

```python
numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]

# Print all numbers in one line
print("Numbers:", end=" ")
for n in numbers:
    print(n, end=" ")
print()   # new line

# Calculate and print stats
```
