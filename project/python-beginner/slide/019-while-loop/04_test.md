# 🔑 Practice: while Loop — Question 3: Password Checker

**Difficulty:** 🟡 Medium

---

## โจทย์

รับรหัสผ่านซ้ำจนกว่าจะพิมพ์ถูก (รหัสคือ `"python123"`)

**Input/Output:**
```
Input: hello
Wrong password! Try again.
Input: test
Wrong password! Try again.
Input: python123
Access granted!
```

---

## 💡 Hint

- ใช้ `while password != "python123":`
- รับ input ต้นรอบ แล้วรับซ้ำในแต่ละรอบ

---

## Starter Code

```python
password = input()

while password != "python123":
    print("Wrong password! Try again.")
    # Get new input

print("Access granted!")
```
