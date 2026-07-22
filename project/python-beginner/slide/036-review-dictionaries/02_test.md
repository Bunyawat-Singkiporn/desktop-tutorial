# 🐛 Practice Review Dictionaries — Question 1: Fix Access Bug

**Difficulty:** 🟢 Easy

---

## โจทย์

โค้ดด้านล่างมีบัค — แก้ให้ทำงานถูกต้อง

```python
# โค้ดที่มีบัค
student = {"name": "Alice", "age": 15}
print(student["score"])   # KeyError!
print(student[name])      # NameError!
```

**Output ที่ถูกต้อง:**
```
Name: Alice
Age: 15
```

---

## 💡 Hint

ตรวจว่า key มีอยู่จริงไหม และใช้ string `"name"` ไม่ใช่ตัวแปร `name`

---

## Starter Code

```python
student = {"name": "Alice", "age": 15}

# แก้โค้ดให้ถูกต้อง
```
