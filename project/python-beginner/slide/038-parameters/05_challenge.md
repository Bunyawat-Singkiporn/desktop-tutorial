# 🔥 Practice Parameters — Question 4: Calculator

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้าง function `calculate(a, b, op)` ที่คำนวณและแสดงผลตาม operator

| op | ผล |
|----|-----|
| `"+"` | a + b |
| `"-"` | a - b |
| `"*"` | a * b |
| `"/"` | a / b (ตรวจว่า b ≠ 0) |

**Output:**
```
3 + 5 = 8
10 - 4 = 6
6 * 7 = 42
10 / 2 = 5.0
10 / 0 = Cannot divide by zero
```

---

## Starter Code

```python
def calculate(a, b, op):
    # Write your code here

calculate(3, 5, "+")
calculate(10, 4, "-")
calculate(6, 7, "*")
calculate(10, 2, "/")
calculate(10, 0, "/")
```
