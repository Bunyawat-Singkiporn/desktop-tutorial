# Practice Function — Question 6: ตั้งรหัสผ่านเกม

**Difficulty:** 🟡 Medium

---

## โจทย์

ระบบสร้างบัญชีเกม: รหัสผ่านต้อง
- ยาวอย่างน้อย 8 ตัว
- มีตัวเลขอย่างน้อย 1 ตัว

สร้าง `is_strong(password)` return `True`/`False`  
แล้วบอกผู้เล่นว่า `Strong password` หรือ `Weak password`

---

## ตัวอย่าง

**Input:**
```
hello123
```

**Output:**
```
Strong password
```

**Input:**
```
abc
```

**Output:**
```
Weak password
```

---

## 💡 Hint

`ch.isdigit()` ใช้เช็คว่าเป็นตัวเลข

---

## Starter Code

```python
def is_strong(password):
    # Write your code here

password = input()
if is_strong(password):
    print("Strong password")
else:
    print("Weak password")
```
