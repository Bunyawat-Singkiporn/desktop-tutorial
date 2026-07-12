# 🔍 Practice: Loop Review — Question 6: Count Value

**Difficulty:** 🟢 Easy

---

## โจทย์

นับว่าตัวเลขที่กำหนดปรากฏกี่ครั้งใน list

```python
scores = [80, 60, 80, 90, 80, 70, 80]
target = 80
```

**Output:**
```
80 appears 4 times
```

---

## 💡 Hint

- วน loop ผ่าน list
- ถ้า `s == target` → `count += 1`

---

## Starter Code

```python
scores = [80, 60, 80, 90, 80, 70, 80]
target = 80
count = 0

for s in scores:
    # Check if s equals target
    # Count it

print(f"{target} appears {count} times")
```
