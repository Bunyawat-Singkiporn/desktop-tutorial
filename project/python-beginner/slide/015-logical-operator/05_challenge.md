# 🔥 Practice and/or/not — Question 4: Theme Park Entry

**Difficulty:** 🔴 Hard

---

## โจทย์

สวนสนุกมีกฎดังนี้:

- **เด็ก** (อายุ < 12): เข้าได้ **เฉพาะเมื่อมีผู้ปกครองมาด้วย**
- **ผู้ใหญ่** (อายุ >= 12): เข้าได้เสมอ **ยกเว้น** ถ้า `banned = True`

รับ:
1. อายุ (int)
2. มีผู้ปกครองมาด้วยหรือไม่ (`True` / `False`)
3. ถูกแบนหรือไม่ (`True` / `False`)

แสดง `Welcome` หรือ `Not Allowed`

> ผสมความรู้: and + or + not + elif

---

## ตัวอย่าง

**Input:**
```
10
True
False
```
**Output:**
```
Welcome
```

**Input:**
```
10
False
False
```
**Output:**
```
Not Allowed
```

**Input:**
```
20
True
True
```
**Output:**
```
Not Allowed
```

---

## 💡 Hint

- แยกเป็น 2 กรณีหลัก: เด็ก vs ผู้ใหญ่
- แต่ละกรณีมีเงื่อนไขต่างกัน

---

## Starter Code

```python
age = int(input())
has_guardian = input()
banned = input()

# Write your code here
```
