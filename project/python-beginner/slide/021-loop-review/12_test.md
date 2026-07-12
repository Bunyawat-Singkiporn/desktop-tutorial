# 📏 Practice: Loop Review — Question 11: Longest Word

**Difficulty:** 🟡 Medium

---

## โจทย์

หา word ที่ยาวที่สุดใน list

```python
words = ["cat", "elephant", "dog", "butterfly", "ox"]
```

**Output:**
```
Longest: butterfly (9)
```

---

## 💡 Hint

- เริ่มจาก `longest = ""`
- ถ้า `len(w) > len(longest)` → อัปเดต `longest = w`

---

## Starter Code

```python
words = ["cat", "elephant", "dog", "butterfly", "ox"]
longest = ""

for w in words:
    # If w is longer than longest, update longest

print(f"Longest: {longest} ({len(longest)})")
```
