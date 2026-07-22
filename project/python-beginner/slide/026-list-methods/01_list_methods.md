# 🛠️ List Methods — การจัดการข้อมูลใน List

---

## List เป็น Mutable

List สามารถ **เปลี่ยนแปลงได้** หลังจากสร้างแล้ว

---

## แก้ไขข้อมูลโดยตรง (Modify by Index)

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'mango']
```

---

## .append() — เพิ่มข้อมูลต่อท้าย

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']
```

---

## .remove() — ลบข้อมูลตามค่า

```python
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)  # ['apple', 'mango']
```

> ถ้าค่าที่ระบุไม่มีอยู่ใน list จะเกิด **ValueError**

---

## .sort() — เรียงข้อมูล

เรียงจาก **น้อยไปมาก** (default):
```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)  # [1, 2, 5, 7, 9]
```

เรียงจาก **มากไปน้อย**:
```python
numbers.sort(reverse=True)
print(numbers)  # [9, 7, 5, 2, 1]
```

---

## สรุป Methods

| Method | หน้าที่ | ตัวอย่าง |
|--------|---------|---------|
| `list[i] = x` | แก้ไขตำแหน่ง i | `fruits[0] = "grape"` |
| `.append(x)` | เพิ่มท้าย | `fruits.append("kiwi")` |
| `.remove(x)` | ลบตามค่า | `fruits.remove("apple")` |
| `.sort()` | เรียงน้อย→มาก | `numbers.sort()` |
| `.sort(reverse=True)` | เรียงมาก→น้อย | `numbers.sort(reverse=True)` |

---

## ตัวอย่างโปรแกรม

```python
scores = [85, 72, 90, 68, 95]
scores.append(80)        # เพิ่มคะแนนใหม่
scores.remove(68)        # ลบคะแนนต่ำสุด
scores.sort(reverse=True)  # เรียงมากไปน้อย
print(scores)
```
