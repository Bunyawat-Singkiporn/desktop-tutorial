# Practice Return — Question 7: คำนวณพื้นที่สนาม

**Difficulty:** 🟡 Medium

---

## โจทย์

โรงเรียนจะทาสีสนามฟุตบอลสี่เหลี่ยม — ต้องรู้พื้นที่

สร้าง `field_area(width, length)` ที่ **return** พื้นที่ (`width * length`)

รับความกว้างและความยาวจาก `input`

---

## ตัวอย่าง

**Input:**
```
20
40
```

**Output:**
```
Football Field
Width: 20.0
Length: 40.0
Area: 800.0
```

---

## Starter Code

```python
def field_area(width, length):
    # Write your code here

width = float(input())
length = float(input())
area = field_area(width, length)
print("Football Field")
print(f"Width: {width}")
print(f"Length: {length}")
print(f"Area: {area}")
```
