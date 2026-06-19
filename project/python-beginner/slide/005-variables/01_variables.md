# 📦 Variables — กล่องเก็บข้อมูล

---

## Variable คืออะไร?

**Variable** คือ "ที่เก็บข้อมูล" ในหน่วยความจำคอมพิวเตอร์

ลองนึกภาพ **กล่องที่มีป้ายชื่อ** 📦:

```
┌─────────────┐
│     12      │  ← ข้อมูลที่เก็บ (value)
└─────────────┘
     age        ← ชื่อกล่อง (variable name)
```

---

## วิธีสร้าง Variable

```python
age = 12
name = "Alex"
price = 99.5
```

> เครื่องหมาย `=` แปลว่า **"เก็บค่า"**
> (ไม่ใช่ "เท่ากับ" แบบในคณิตศาสตร์)

---

## วิธีใช้ Variable

```python
name = "Alex"
print(name)              # แสดงค่าใน variable
print("Hello,", name)    # ใช้ร่วมกับข้อความ
```

ผลลัพธ์:
```
Alex
Hello, Alex
```

---

## เปลี่ยนค่า Variable ได้

```python
score = 0
print(score)   # 0

score = 100
print(score)   # 100
```

> กล่องเดิม แต่ใส่ของใหม่เข้าไปได้เสมอ

---

## Variable บวกค่าได้

```python
price = 100
tax = 7
total = price + tax

print("Price:", price)
print("Tax:", tax)
print("Total:", total)
```

ผลลัพธ์:
```
Price: 100
Tax: 7
Total: 107
```

---

## ตัวอย่างโปรแกรม

```python
name = "Sarah"
age = 13
city = "Bangkok"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

ผลลัพธ์:
```
Name: Sarah
Age: 13
City: Bangkok
```

---

## สิ่งที่ควรจำ

| ทำได้ ✅ | ทำไม่ได้ ❌ |
|---------|-----------|
| `name = "Alex"` | `"Alex" = name` |
| `score = 100` | `100 = score` |
| เปลี่ยนค่าได้ตลอด | ค่าซ้ายต้องเป็นชื่อ variable |
