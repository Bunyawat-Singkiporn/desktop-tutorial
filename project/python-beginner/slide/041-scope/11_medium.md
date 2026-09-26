# 🔭 Scope — ข้อ 11: เติมเงินกระเป๋า

**Difficulty:** 🟡 Medium

---

## โจทย์

เงินในกระเป๋าเป็น global

**เงื่อนไข:**

- `money = 100`
- `deposit(n)` เพิ่มเงินด้วย global
- เติม 50 แล้วพิมพ์ money

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
150
```


---

## 💡 Hint

global ก่อนแก้ค่า

---

## Starter Code

```python
money = 100

def deposit(n):
    # global

deposit(50)
print(money)
```
