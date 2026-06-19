# 🧾 Practice: Type Conversion — Question 3: Fix the TypeError

**Difficulty:** 🟡 Medium

---

## โจทย์

โค้ดด้านล่างมี TypeError — **แก้ให้รันได้** โดยไม่เปลี่ยน Output

```python
student_name = input()
score = input()
passed_score = 50

print("Name: " + student_name)
print("Score: " + score)
print("Pass score: " + passed_score)
```

**Input:**
```
Emma
75
```

**Output:**
```
Name: Emma
Score: 75
Pass score: 50
```

---

## 💡 Hint

ไม่สามารถต่อ `str` กับ `int` ด้วย `+` — ต้องแปลง `int` เป็น `str` ก่อน

---

## Starter Code

```python
student_name = input()
score = input()
passed_score = 50

print("Name: " + student_name)
print("Score: " + score)
print("Pass score: " + passed_score)  # ← ตรงนี้มี Error!
```
