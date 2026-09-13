# Practice Function — Medium: แปลอุณหภูมิแบบเลือกได้

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง:
- `to_f(c)` return Fahrenheit
- `to_c(f)` return Celsius (`(f - 32) * 5/9`)

รับโหมด `F` หรือ `C` และตัวเลขจาก input แล้วแปลงตามโหมด

> ผสมความรู้: return + input + if/elif + float

---

## ตัวอย่าง

**Input:**
```
F
100
```

**Output:**
```
37.78 C
```

(ใช้ `:.2f`)

**Input:**
```
C
0
```

**Output:**
```
32.00 F
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

if mode == "C":
    print(f"{to_f(value):.2f} F")
elif mode == "F":
    print(f"{to_c(value):.2f} C")
else:
    print("Unknown mode")
```
