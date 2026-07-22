# 🔒 Tuples — ข้อมูลที่ไม่เปลี่ยนแปลง

---

## Tuple คืออะไร?

Tuple คือโครงสร้างข้อมูลที่คล้าย List แต่ **ไม่สามารถแก้ไขได้** หลังจากสร้างแล้ว (Immutable)

---

## การสร้าง Tuple

ใช้วงเล็บ `()` แทน `[]`

```python
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
point = (10, 20)
student = ("Alice", 15, "Grade 9")
```

---

## การเข้าถึงข้อมูล (เหมือน List)

```python
days = ("Mon", "Tue", "Wed")

print(days[0])   # Mon
print(days[-1])  # Wed
print(len(days)) # 3
```

---

## วนซ้ำด้วย for loop

```python
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
    print(day)
```

---

## Immutable — ห้ามแก้ไข

```python
days = ("Mon", "Tue", "Wed")
days[0] = "Sunday"  # ❌ TypeError!
```

> Tuple ถูกออกแบบมาเพื่อข้อมูลที่ **ไม่ควรเปลี่ยน**

---

## เมื่อไหร่ควรใช้ Tuple?

| ใช้ **List** เมื่อ | ใช้ **Tuple** เมื่อ |
|------------------|-------------------|
| ต้องการเพิ่ม/ลบข้อมูล | ข้อมูลคงที่ ไม่ต้องเปลี่ยน |
| ข้อมูลเปลี่ยนได้ | ต้องการป้องกันการแก้ไข |
| รายการสินค้า | วันในสัปดาห์, พิกัด, ข้อมูลนักเรียน |

---

## ตัวอย่างโปรแกรม

```python
student = ("Bob", 14, "Grade 8")

print("Name:", student[0])
print("Age:", student[1])
print("Grade:", student[2])
```

**Output:**
```
Name: Bob
Age: 14
Grade: Grade 8
```
