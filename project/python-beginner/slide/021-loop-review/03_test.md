# 🔢 Practice: Loop Review — Question 2: Multiples

**Difficulty:** 🟡 Medium

---

## โจทย์

รับตัวเลข n แล้วแสดงตัวคูณของ n ตั้งแต่ 1–10

**Input:**
```
7
```

**Output:**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## 💡 Hint

- `for i in range(1, 11):`
- ใช้ f-string: `f"{n} x {i} = {n * i}"`

---

## Starter Code

```python
n = int(input())

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
