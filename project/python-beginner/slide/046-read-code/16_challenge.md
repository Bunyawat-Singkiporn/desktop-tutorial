# 👀 Read Code — ข้อ 16: มือถือ trace ยาว

**Difficulty:** 🔴 Challenge

---

## โจทย์

จำลองยอดเงิน: เริ่ม 100 ซื้อของราคาใน list `[20, 15, 30]` ทีละรายการ แล้วพิมพ์ยอดคงเหลือ

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
35
```


---

## 💡 Hint

หักทีละรายการตามลำดับ

---

## Starter Code

```python
money = 100
for price in [20, 15, 30]:
    money = money - price
print(money)
```
