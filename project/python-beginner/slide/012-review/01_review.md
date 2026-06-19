# 🔁 Review — ทบทวนทุกอย่าง

---

## สิ่งที่เรียนมาตลอด 11 สัปดาห์

| สัปดาห์ | หัวข้อ | สิ่งสำคัญที่สุด |
|--------|--------|--------------|
| 1 | What is Python | `print("Hello")` |
| 2 | Environment | อ่าน Error → แก้ได้ |
| 3 | Syntax | ตัวเล็ก, ครบคู่, ไม่ indent เกิน |
| 4 | Comments | `# อธิบายโค้ด` |
| 5 | Variables | `name = "Alice"` |
| 6 | Naming Rules | snake_case, สื่อความหมาย |
| 7 | Data Types | int, float, str, bool |
| 8 | Type Conversion | `int()`, `float()`, `str()` |
| 9 | Input | `name = input()` |
| 10 | Output Formatting | `f"Hello {name}"` |
| 11 | Operators | `+`, `-`, `*`, `/`, `%`, `**` |

---

## ตัวอย่างโปรแกรมที่รวมทุกอย่าง

```python
# รับข้อมูลจากผู้ใช้
name = input()
age = int(input())
price = float(input())

# คำนวณ
price_with_vat = price * 1.07

# แสดงผล
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price + VAT: {price_with_vat:.2f} baht")
```

Input:
```
Alice
13
100
```

Output:
```
Name: Alice
Age: 13
Price + VAT: 107.00 baht
```

---

## สูตรโปรแกรมพื้นฐาน

```
1. รับข้อมูล    → input()
2. ประมวลผล    → operators, variables
3. แสดงผล     → print() / f-string
```

---

## Checklist ก่อนส่งงาน

- [ ] ตั้งชื่อ variable เป็น snake_case
- [ ] แปลง `input()` เป็น `int()` หรือ `float()` ก่อนคำนวณ
- [ ] ใช้ f-string สำหรับ output ที่มี variable
- [ ] มี comment อธิบายส่วนสำคัญ
- [ ] ทดสอบด้วย input หลายค่า

---

## ข้อผิดพลาดที่พบบ่อย

| ข้อผิดพลาด | สาเหตุ | วิธีแก้ |
|-----------|--------|--------|
| `NameError` | ใช้ `Print` แทน `print` | ใช้ตัวพิมพ์เล็กเสมอ |
| `TypeError` | `"5" + 5` | แปลงด้วย `int()` หรือ `str()` |
| `SyntaxError` | ขาด `)` หรือ `"` | ตรวจให้ครบคู่ |

---

## ยินดีด้วย! 🎉

คุณผ่านพื้นฐาน Python ครบแล้ว! บทต่อไปจะเรียน:

- **Even / Odd** — `%` และ `if/else`
- **elif** — เงื่อนไขหลายกรณี
- **Logical Operators** — `and`, `or`, `not`
- **For Loop** — วนซ้ำ
