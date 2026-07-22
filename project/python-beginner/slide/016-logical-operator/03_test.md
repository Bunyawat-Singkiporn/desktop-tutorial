# 🏷️ Practice and/or/not — Question 2: Discount

**Difficulty:** 🟡 Medium

---

## โจทย์

รับจำนวนเงินและสถานะสมาชิก แล้วตรวจสอบว่าได้รับส่วนลดหรือไม่

**เงื่อนไข:** ต้องผ่าน **ทั้งสอง** ข้อ
- เงิน >= 100
- เป็นสมาชิก (`True`)

| ผล | Output |
|----|--------|
| ผ่านทั้งคู่ | `Discount` |
| ไม่ผ่าน | ไม่แสดงอะไร |

---

## ตัวอย่าง

**Input:**
```
150
True
```

**Output:**
```
Discount
```

---

## 💡 Hint

ค่าที่รับมาจาก `input()` จะเป็น string เสมอ ต้องเปรียบเทียบกับ `"True"`

---

## Starter Code

```python
money = int(input())
member = input()

# Write your code here
```
