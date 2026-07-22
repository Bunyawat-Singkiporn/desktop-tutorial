# 📊 Practice Dictionary — Question 1: Word Counter

**Difficulty:** 🟢 Easy

---

## โจทย์

นับว่าแต่ละคำปรากฏกี่ครั้งใน list

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
```

**Output:**
```
cat: 3
dog: 2
bird: 1
```

---

## 💡 Hint

ถ้า `word` อยู่ใน dict แล้ว → เพิ่ม 1
ถ้ายังไม่มี → ตั้งค่าเป็น 1

---

## Starter Code

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}

for word in words:
    # Write your code here

for word, n in count.items():
    print(f"{word}: {n}")
```
