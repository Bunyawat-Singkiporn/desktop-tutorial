# 🔥 Practice: Debugging Loops — Question 4: Fix the Broken Report

**Difficulty:** 🔴 Hard

---

## โจทย์

โค้ดด้านล่างมี **4 bugs** แก้ให้ทำงานถูกต้อง

```python
scores = [80, 95, 60, 45, 75]
total = 0
count = 0

for score in scores:
total = total + score
count = count + 1

average = total / count
print(f"Total: {total}")
  print(f"Count: {count}")
print(f"Average: {average:.1f}")
print(f"Max: {max(score)}")
```

**Output ที่ต้องการ:**
```
Total: 355
Count: 5
Average: 71.0
Max: 95
```

---

## 💡 Hint

- Bug 1: Indent ผิดใน loop body
- Bug 2: Indent ผิดของ print
- Bug 3: `max(score)` ควรเป็น `max(scores)`

---

## Starter Code

```python
scores = [80, 95, 60, 45, 75]
total = 0
count = 0

for score in scores:
total = total + score   # Bug 1: indent
count = count + 1       # Bug 1: indent

average = total / count
print(f"Total: {total}")
  print(f"Count: {count}")   # Bug 2: indent
print(f"Average: {average:.1f}")
print(f"Max: {max(score)}")  # Bug 3: wrong variable
```
