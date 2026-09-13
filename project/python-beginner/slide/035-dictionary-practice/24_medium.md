# Practice Dictionary — Question 23: ใครคะแนนสูงสุด

**Difficulty:** 🟡 Medium

---

## โจทย์

หาคนที่ได้คะแนนสูงสุดในห้อง

```python
scores = {"Alice": 85, "Bob": 92, "Cara": 78}
```

**Output:**
```
Top: Bob (92)
```

---

## 💡 Hint

วน loop เก็บชื่อและคะแนนสูงสุดไว้ในตัวแปร

---

## Starter Code

```python
scores = {"Alice": 85, "Bob": 92, "Cara": 78}

top_name = ""
top_score = -1

for name, score in scores.items():
    # Write your code here

print(f"Top: {top_name} ({top_score})")
```
