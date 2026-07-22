# 🐛 Practice: Debugging Loops — Question 3: Fix Three Bugs

**Difficulty:** 🟡 Medium

---

## โจทย์

โค้ดด้านล่างมี **3 bugs** แก้ให้แสดงผลถูกต้อง

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(names)

total = 0
for i in range(1, 5):
    total = total + i
print("Total 1-5:", total)
```

**Output ที่ต้องการ:**
```
Alice
Bob
Charlie
Total 1-5: 15
```

---

## 💡 Hint

Bug 1: ใช้ `names` แทน `name`
Bug 2: `range(1, 5)` ได้แค่ 1–4
Bug 3: `print` อยู่นอก loop แต่ค่า total ผิด

---

## Starter Code

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(names)   # Bug 1

total = 0
for i in range(1, 5):   # Bug 2
    total = total + i
print("Total 1-5:", total)
```
