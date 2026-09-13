# Practice Function — Medium: ตรวจรหัสผ่าน

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `is_strong(password)` ที่ return `True` ถ้า:
- ความยาว >= 8 **และ**
- มีตัวเลขอย่างน้อย 1 ตัว

ไม่งั้น return `False`

โปรแกรมหลักถามรหัสผ่าน แล้วพิมพ์ `Strong` หรือ `Weak`

> ผสมความรู้: return + input + if + for + str

---

## ตัวอย่าง

**Input:**
```
hello123
```

**Output:**
```
Strong
```

**Input:**
```
abc
```

**Output:**
```
Weak
```

---

## 💡 Hint

เช็คตัวเลข: `for ch in password:` แล้วใช้ `ch.isdigit()`

---

## Starter Code

```python
def is_strong(password):
    # Write your code here

password = input()
if is_strong(password):
    print("Strong")
else:
    print("Weak")
```
