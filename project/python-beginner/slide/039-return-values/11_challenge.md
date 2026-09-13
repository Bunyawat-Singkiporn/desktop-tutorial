# 🔥 Practice Return — Challenge: สมัคร username เกม

**Difficulty:** 🔴 Hard

---

## โจทย์

ระบบสมัครเกม: username ต้องยาวอย่างน้อย 8 ตัวอักษร

สร้าง 2 functions:
1. `name_length(text)` — return ความยาว
2. `can_register(text)` — return `True` ถ้ายาว >= 8 (เรียก `name_length` ข้างใน)

รับ username แล้วบอกผล

---

## ตัวอย่าง

**Input:**
```
dragon123
```

**Output:**
```
Username: dragon123
Length: 9
Status: OK to register
```

**Input:**
```
cat
```

**Output:**
```
Username: cat
Length: 3
Status: Too short
```

---

## Starter Code

```python
def name_length(text):
    # Write your code here

def can_register(text):
    # Write your code here

username = input()
print(f"Username: {username}")
print(f"Length: {name_length(username)}")
if can_register(username):
    print("Status: OK to register")
else:
    print("Status: Too short")
```
