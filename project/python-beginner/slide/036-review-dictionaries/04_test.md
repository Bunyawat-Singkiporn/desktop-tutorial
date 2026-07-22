# 🤝 Practice Review Dictionaries — Question 3: Merge Dicts

**Difficulty:** 🟡 Medium

---

## โจทย์

รวม dict สองอันเข้าด้วยกัน (ถ้า key ซ้ำให้ใช้ค่าจาก `extra`)

```python
base = {"name": "Alice", "age": 15}
extra = {"score": 90, "age": 16}
```

**Output:**
```
{'name': 'Alice', 'age': 16, 'score': 90}
```

---

## 💡 Hint

ใช้ `.update(extra)` เพื่อรวม — ค่าใหม่จะทับค่าเดิมถ้า key ซ้ำ

---

## Starter Code

```python
base = {"name": "Alice", "age": 15}
extra = {"score": 90, "age": 16}

# รวม extra เข้า base

print(base)
```
