# Practice Parameters — Medium: อายุ + สิทธิ์โหวต

**Difficulty:** 🟡 Medium

---

## โจทย์

1. รับอายุด้วย `input` แปลงเป็น `int`
2. สร้าง function `check_vote(age)` ที่แสดงผล:
   - อายุ >= 18 → `You can vote`
   - น้อยกว่า → `Too young to vote`
3. เรียก `check_vote(age)` ด้วยค่าที่รับมา

> ผสมความรู้: parameter + input + int() + if/else

---

## ตัวอย่าง

**Input:**
```
20
```

**Output:**
```
You can vote
```

**Input:**
```
15
```

**Output:**
```
Too young to vote
```

---

## Starter Code

```python
def check_vote(age):
    # Write your code here

age = int(input())
check_vote(age)
```
