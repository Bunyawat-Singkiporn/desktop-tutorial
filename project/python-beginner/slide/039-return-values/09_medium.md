# Practice Return — Question 8: แอพอากาศสำหรับทริป

**Difficulty:** 🟡 Medium

---

## โจทย์

แอพท่องเที่ยวต้องแปลง °C เป็น °F

สร้าง `to_fahrenheit(c)` ที่ **return** ค่า Fahrenheit  
สูตร: `c * 9/5 + 32`

---

## ตัวอย่าง

**Input:**
```
0
```

**Output:**
```
Trip Weather
0.0 C = 32.0 F
```

---

## Starter Code

```python
def to_fahrenheit(c):
    # Write your code here

c = float(input())
f = to_fahrenheit(c)
print("Trip Weather")
print(f"{c} C = {f} F")
```
