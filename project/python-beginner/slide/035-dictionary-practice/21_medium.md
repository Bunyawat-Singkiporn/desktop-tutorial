# Practice Dictionary — Question 20: Login เข้าแอพ

**Difficulty:** 🟡 Medium

---

## โจทย์

มีบัญชีผู้ใช้ในระบบ:

```python
accounts = {"alice": "1234", "bob": "abcd"}
```

รับ username และ password  
ถ้าตรง → `Welcome!`  
ถ้า user ไม่มี หรือรหัสผิด → `Login failed`

---

## ตัวอย่าง

**Input:**
```
alice
1234
```

**Output:**
```
Welcome!
```

**Input:**
```
alice
0000
```

**Output:**
```
Login failed
```

---

## Starter Code

```python
accounts = {"alice": "1234", "bob": "abcd"}

user = input()
password = input()
# Write your code here
```
