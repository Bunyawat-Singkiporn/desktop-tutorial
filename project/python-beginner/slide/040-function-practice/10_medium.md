# Practice Function — Medium: เครื่องคิดเลขเมนู

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง functions:
- `add(a, b)` return ผลบวก
- `mul(a, b)` return ผลคูณ

โปรแกรมหลัก:
1. รับ `a`, `b` จาก input
2. รับตัวเลือก `1` = บวก, `2` = คูณ
3. เรียก function ที่ถูกแล้วพิมพ์ผล

> ผสมความรู้: return + input + if/elif + operators

---

## ตัวอย่าง

**Input:**
```
7
3
1
```

**Output:**
```
Result: 10
```

---

## Starter Code

```python
def add(a, b):
    # Write your code here

def mul(a, b):
    # Write your code here

a = int(input())
b = int(input())
choice = input()

if choice == "1":
    print(f"Result: {add(a, b)}")
elif choice == "2":
    print(f"Result: {mul(a, b)}")
else:
    print("Invalid")
```
