# 🔥 Practice: Nested Loops — Question 4: Number Pattern

**Difficulty:** 🔴 Hard

---

## โจทย์

รับ n แล้วแสดง pattern ตัวเลขตามรูปแบบนี้

**Input:**
```
4
```

**Output:**
```
1
1 2
1 2 3
1 2 3 4
```

**Input:**
```
5
```

**Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## 💡 Hint

- Loop นอก: แถว 1–n
- Loop ใน: ตัวเลข 1 ถึง แถวปัจจุบัน
- `print(j, end=" ")` แล้ว `print()` ขึ้นบรรทัดใหม่

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    for j in range(1, row + 1):
        print(j, end=" ")
    print()
```
