# 💰 Practice: Loop Review — Question 13: Collect Inputs

**Difficulty:** 🟡 Medium

---

## โจทย์

ใช้ while loop รับตัวเลข 5 ครั้ง แล้วแสดงค่าเฉลี่ย

**Input:**
```
70
85
90
60
95
```

**Output:**
```
Average: 80.0
```

---

## 💡 Hint

- ใช้ `while len(numbers) < 5:` วนจนมี 5 ตัว
- `numbers.append(n)` เก็บค่า
- `sum(numbers) / len(numbers)` หาเฉลี่ย

---

## Starter Code

```python
numbers = []

while len(numbers) < 5:
    n = int(input())
    # Append n to numbers

print(f"Average: {sum(numbers)/len(numbers):.1f}")
```
