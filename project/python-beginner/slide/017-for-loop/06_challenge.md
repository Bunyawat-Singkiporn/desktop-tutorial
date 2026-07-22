# 🔥 Practice for Loop — Question 4: Multiplication Table

**Difficulty:** 🔴 Hard

---

## โจทย์

รับตัวเลข N แล้วแสดง **ตารางสูตรคูณ** ของ N ตั้งแต่ 1 ถึง 10

> ผสมความรู้: for loop + range + input + string formatting

---

## ตัวอย่าง

**Input:**
```
3
```

**Output:**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

---

## 💡 Hint

- ใช้ `range(1, 11)` วนรอบ 1 ถึง 10
- คำนวณ `n * i` ในแต่ละรอบ
- ใช้ `print(f"...")` หรือ `print(n, "x", i, "=", n * i)`

---

## Starter Code

```python
n = int(input())

for i in range(1, 11):
    # Write your code here
```
