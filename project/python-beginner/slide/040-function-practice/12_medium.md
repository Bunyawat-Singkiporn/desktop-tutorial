# Practice Function — Question 10: ตัวช่วยแปลงอุณหภูมิท่องเที่ยว

**Difficulty:** 🟡 Medium

---

## โจทย์

แอพท่องเที่ยว: ผู้ใช้เลือกโหมดแล้วแปลงอุณหภูมิ

- พิมพ์ `C` แล้วใส่ค่า → แปลงเป็น °F
- พิมพ์ `F` แล้วใส่ค่า → แปลงเป็น °C

สร้าง `to_f(c)` และ `to_c(f)` ที่ return ค่า

---

## ตัวอย่าง

**Input:**
```
C
0
```

**Output:**
```
Travel Helper
0.0 C = 32.00 F
```

---

## Starter Code

```python
def to_f(c):
    # Write your code here

def to_c(f):
    # Write your code here

mode = input()
value = float(input())
print("Travel Helper")
if mode == "C":
    print(f"{value} C = {to_f(value):.2f} F")
elif mode == "F":
    print(f"{value} F = {to_c(value):.2f} C")
else:
    print("Unknown mode")
```
