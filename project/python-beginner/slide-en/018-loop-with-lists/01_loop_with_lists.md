# 📋 Loop with Lists — วนซ้ำกับข้อมูลหลายชิ้น

---

## List คืออะไร?

**List** คือการเก็บข้อมูลหลายชิ้นไว้ในตัวแปรเดียว

```python
fruits = ["Apple", "Banana", "Mango"]
```

| Index | ค่า |
|-------|-----|
| `[0]` | `"Apple"` |
| `[1]` | `"Banana"` |
| `[2]` | `"Mango"` |

> Index เริ่มที่ **0** เสมอ

---

## วนซ้ำ List ด้วย for

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

ผลลัพธ์:
```
Apple
Banana
Mango
```

> `fruit` คือตัวแปรชั่วคราวที่เก็บค่าแต่ละรอบ — ตั้งชื่ออะไรก็ได้

---

## รวมตัวเลขใน List

```python
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total = total + score

print("Total:", total)
print("Count:", len(scores))
print(f"Average: {total / len(scores):.1f}")
```

ผลลัพธ์:
```
Total: 438
Count: 5
Average: 87.6
```

---

## for vs range

```python
# range — รู้จำนวนรอบ
for i in range(3):
    print(i)      # 0, 1, 2

# list — วนผ่านแต่ละค่า
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(color)  # Red, Green, Blue
```

---

## len() — นับจำนวนสมาชิก

```python
names = ["Alice", "Bob", "Charlie"]
print(len(names))   # 3

numbers = [10, 20, 30, 40, 50]
print(len(numbers)) # 5
```

---

## สรุป

| เรื่อง | ตัวอย่าง |
|-------|---------|
| สร้าง list | `items = ["a", "b", "c"]` |
| เข้าถึงสมาชิก | `items[0]` → `"a"` |
| วนซ้ำ list | `for item in items:` |
| นับจำนวน | `len(items)` → `3` |
