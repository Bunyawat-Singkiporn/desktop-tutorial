# 📐 Practice: Nested Loops — Question 2: Right Triangle

**Difficulty:** 🟡 Medium

---

## โจทย์

รับจำนวนแถว แล้วแสดงสามเหลี่ยมมุมฉาก

**Input:**
```
5
```

**Output:**
```
*
**
***
****
*****
```

---

## 💡 Hint

- Loop นอก: `for row in range(1, n+1)`
- Loop ใน: `for col in range(row)` — วนตามแถวปัจจุบัน

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        # Print one * without newline
    # Move to next line
```
