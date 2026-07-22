# 🔄 Practice Review Dictionaries — Question 2: List to Dict

**Difficulty:** 🟡 Medium

---

## โจทย์

แปลง list ของคู่ `[ชื่อ, คะแนน]` ให้เป็น dict

```python
data = [["Alice", 90], ["Bob", 75], ["Charlie", 88]]
```

**Output:**
```
{'Alice': 90, 'Bob': 75, 'Charlie': 88}
```

---

## 💡 Hint

Loop ผ่าน `data` และกำหนด `scores[pair[0]] = pair[1]`

---

## Starter Code

```python
data = [["Alice", 90], ["Bob", 75], ["Charlie", 88]]
scores = {}

# แปลงเป็น dict

print(scores)
```
