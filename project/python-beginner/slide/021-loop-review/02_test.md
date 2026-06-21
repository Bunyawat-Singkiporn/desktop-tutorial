# 🔁 Practice: Loop Review — Question 1: Sum with for

**Difficulty:** 🟢 Easy

---

## โจทย์

รับ n แล้วรวมตัวเลขตั้งแต่ 1 ถึง n

**Input:**
```
5
```

**Output:**
```
Sum from 1 to 5 = 15
```

---

## 💡 Hint

- ใช้ `for i in range(1, n+1):`
- สะสมใน `total`

---

## Starter Code

```python
n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i

print(f"Sum from 1 to {n} = {total}")
```
