# 🎨 Output Formatting — จัดรูปแบบการแสดงผล

---

## ปัญหาการต่อข้อความแบบเดิม

```python
name = "Alice"
age = 13
# วิธีเก่า — ยุ่งยากและอ่านยาก
print("My name is " + name + " and I am " + str(age) + " years old.")
```

---

## f-string คืออะไร?

**f-string** คือวิธีใส่ค่า variable เข้าไปในข้อความโดยตรง — สะดวกกว่ามาก!

```python
name = "Alice"
age = 13
print(f"My name is {name} and I am {age} years old.")
```

Output:
```
My name is Alice and I am 13 years old.
```

---

## วิธีใช้ f-string

1. ใส่ตัวอักษร `f` ก่อนเครื่องหมาย `"`
2. ใส่ variable ในวงเล็บปีกกา `{}`

```python
price = 250
discount = 50
final = price - discount

print(f"Original: {price} baht")
print(f"Discount: {discount} baht")
print(f"Final:    {final} baht")
```

Output:
```
Original: 250 baht
Discount: 50 baht
Final:    200 baht
```

---

## Format ทศนิยม :.2f

```python
pi = 3.14159
price = 99.9

print(f"Pi = {pi:.2f}")       # แสดง 2 ตำแหน่ง → 3.14
print(f"Price: {price:.2f}")  # → 99.90
```

Output:
```
Pi = 3.14
Price: 99.90
```

> `:.2f` แปลว่า "ทศนิยม 2 ตำแหน่ง"

---

## sep= และ end=

```python
# sep= กำหนดตัวคั่นระหว่างค่า
print("A", "B", "C", sep="-")        # A-B-C
print("A", "B", "C", sep=" | ")      # A | B | C

# end= กำหนดตัวท้าย (ค่าปกติคือ "\n" = ขึ้นบรรทัดใหม่)
print("Hello", end=" ")
print("World")                        # Hello World (บรรทัดเดียว)
```

---

## เปรียบเทียบ: ก่อน vs หลังใช้ f-string

```python
name = "Sam"
score = 95
grade = "A"

# ❌ แบบเดิม
print("Name: " + name + " | Score: " + str(score) + " | Grade: " + grade)

# ✅ f-string
print(f"Name: {name} | Score: {score} | Grade: {grade}")
```

Output เหมือนกัน:
```
Name: Sam | Score: 95 | Grade: A
```

---

## สรุป

| วิธี | ตัวอย่าง |
|-----|---------|
| `print("text", var)` | ง่ายสุด แต่จัดรูปแบบยาก |
| `f"text {var}"` | ✅ แนะนำ — อ่านง่าย จัดรูปแบบได้ |
| `{var:.2f}` | ทศนิยม 2 ตำแหน่ง |
