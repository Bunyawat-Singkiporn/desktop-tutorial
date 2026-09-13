# Practice Dictionary — Question 19: นับผลไม้ในตะกร้า

**Difficulty:** 🟡 Medium

---

## โจทย์

นับว่าผลไม้แต่ละชนิดมีกี่ลูก

```python
basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
```

**Output:**
```
apple: 3
banana: 2
mango: 1
```

---

## 💡 Hint

เหมือน Word Counter — ถ้ามีใน dict แล้ว `+= 1` ถ้ายังไม่มีตั้งเป็น `1`

---

## Starter Code

```python
basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
count = {}

for fruit in basket:
    # Write your code here

for fruit, n in count.items():
    print(f"{fruit}: {n}")
```
