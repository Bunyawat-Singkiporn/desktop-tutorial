# 🧩 Function Practice — ข้อ 22: ถอนเงินที่ตู้ ATM

**Difficulty:** 🟡 Medium

---

## โจทย์

ตู้ ATM ต้องเช็คว่าเงินในบัญชีพอถอนหรือไม่
ถ้ายอดพอ ให้คืนยอดใหม่หลังถอน ถ้าไม่พอให้คงยอดเดิมไว้

รับยอดเงินคงเหลือกับจำนวนที่อยากถอน

**เงื่อนไข:**

- `can_withdraw(balance, amount)` คืน `True` ถ้ายอดพอ ไม่งั้น `False`
- `new_balance(balance, amount)` คืนยอดใหม่หลังถอน ถ้าถอนไม่ได้ให้คืนยอดเดิม
- ถ้ารถอนได้พิมพ์ `Success` และยอดใหม่
- ถ้ารถอนไม่ได้พิมพ์ `Not enough` และยอดเดิม

---

## Input

2 บรรทัด — ยอดคงเหลือ และจำนวนที่ถอน

## Output

2 บรรทัด — สถานะ และยอดเงิน

---

## ตัวอย่าง

**Input:**

```text
500
200
```

**Output:**

```text
Success
300
```

---

## 💡 Hint

ใช้ผลจาก `can_withdraw` ช่วยตัดสินใจก่อนเรียก `new_balance`

---

## Starter Code

```python
def can_withdraw(balance, amount):
    # เขียนโค้ดตรงนี้

def new_balance(balance, amount):
    # เขียนโค้ดตรงนี้

balance = int(input())
amount = int(input())

# เขียนโค้ดตรงนี้
```
