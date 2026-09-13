# Practice Function — Question 8: แอพเครื่องคิดเลขมือถือ

**Difficulty:** 🟡 Medium

---

## โจทย์

ทำแอพเครื่องคิดเลขง่ายๆ

- `add(a, b)` return ผลบวก
- `mul(a, b)` return ผลคูณ

ผู้ใช้พิมพ์เลข 2 ตัว แล้วเลือก:
- `1` = บวก
- `2` = คูณ

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
Calculator
7 + 3 = 10
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
print("Calculator")
if choice == "1":
    print(f"{a} + {b} = {add(a, b)}")
elif choice == "2":
    print(f"{a} * {b} = {mul(a, b)}")
else:
    print("Unknown button")
```
