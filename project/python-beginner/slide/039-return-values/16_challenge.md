# ↩️ Return Values — ข้อ 16: สรุปออเดอร์อาหาร

**Difficulty:** 🔴 Challenge

---

## โจทย์

คำนวณราคารวมแล้วคิด VAT 7%

**เงื่อนไข:**

- สร้าง `subtotal(a, b)` คืน a+b
- สร้าง `with_vat(amount)` คืน amount * 1.07
- พิมพ์ `with_vat(subtotal(100, 50))` ด้วยทศนิยม 2 ตำแหน่ง

---

## ตัวอย่าง

**Output:**

```text
160.50
```


---

## 💡 Hint

ประกอบสองฟังก์ชันด้วย return

---

## Starter Code

```python
def subtotal(a, b):
    # return
    # เขียนโค้ดตรงนี้

def with_vat(amount):
    # return
    # เขียนโค้ดตรงนี้

print(f"{with_vat(subtotal(100, 50)):.2f}")
```
