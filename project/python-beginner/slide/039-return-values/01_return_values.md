# 📤 Return Values — ค่าที่ส่งกลับจาก Function

---

## return คืออะไร?

`return` ส่งค่า **กลับออกมา** จาก function เพื่อนำไปใช้ต่อ

---

## print vs return

```python
# แบบ print — แสดงผลแต่นำไปใช้ต่อไม่ได้
def add_print(a, b):
    print(a + b)

result = add_print(3, 5)
print(result)    # None  ← ไม่มีค่าส่งกลับ!
```

```python
# แบบ return — นำไปใช้ต่อได้
def add_return(a, b):
    return a + b

result = add_return(3, 5)
print(result)    # 8  ✅
```

---

## การใช้ return

```python
def square(n):
    return n * n

result = square(5)
print(result)      # 25
print(square(4))   # 16
```

---

## return กับ if/else

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))   # True
print(is_even(7))   # False
```

---

## return กับ Grade

```python
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

grade = get_grade(85)
print(f"Grade: {grade}")  # Grade: A
```

---

## ข้อสำคัญ

- `return` หยุดการทำงานของ function ทันที
- Function ที่ไม่มี `return` จะคืนค่า `None`
- สามารถเก็บค่าที่ return ได้: `result = func()`
