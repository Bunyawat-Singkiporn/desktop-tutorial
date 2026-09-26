# ↩️ Return Values — ข้อ 14: สถานะกระเป๋าเงิน

**Difficulty:** 🔴 Challenge

---

## โจทย์

สถานะเงินในกระเป๋า

**เงื่อนไข:**

- สร้าง `wallet_status(money)` คืน `Broke` ถ้า money < 50, `OK` ถ้า < 200, ไม่งั้น `Rich`
- พิมพ์ผลของ `30` `120` `500`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)

## Output

3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Broke
OK
Rich
```


---

## 💡 Hint

ใช้ elif หลายขั้น คืนสตริง

---

## Starter Code

```python
def wallet_status(money):
    # return
    # เขียนโค้ดตรงนี้

print(wallet_status(30))
print(wallet_status(120))
print(wallet_status(500))
```
