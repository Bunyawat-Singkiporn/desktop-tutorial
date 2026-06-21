# 🔍 Practice: Loop Safety — Question 3: Find First Match

**Difficulty:** 🟡 Medium

---

## โจทย์

วนซ้ำ list แล้วหยุดเมื่อเจอชื่อที่ต้องการ

```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
```

รับชื่อจากผู้ใช้ แล้วแสดงว่าเจอที่ตำแหน่งเท่าไหร่ (เริ่มนับที่ 1)

**Input:**
```
Charlie
```

**Output:**
```
Found Charlie at position 3
```

**Input:**
```
Zara
```

**Output:**
```
Zara not found
```

---

## 💡 Hint

- ใช้ตัวแปร `found = False`
- ถ้าเจอ: แสดงตำแหน่ง, `found = True`, `break`
- หลัง loop: ถ้า `not found` แสดง not found

---

## Starter Code

```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = input()

for i in range(len(names)):
    if names[i] == target:
        # Print position (i+1) and stop searching

# If never found, print "target not found"
```
