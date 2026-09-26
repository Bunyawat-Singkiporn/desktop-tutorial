# 🔁 Practice Review — ข้อ 14: คลังสินค้า

**Difficulty:** 🔴 Challenge

---

## โจทย์

จัดการจำนวนสินค้าใน dict

**เงื่อนไข:**

- `add_stock(inv, item, n)` เพิ่มจำนวน (ถ้ายังไม่มีให้เริ่ม 0)
- เริ่ม `{}` เพิ่ม apple 3 สองครั้ง แล้วพิมพ์ inv

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
{'apple': 6}
```


---

## 💡 Hint

เช็ก key ก่อนบวก

---

## Starter Code

```python
def add_stock(inv, item, n):
    # เพิ่มสต็อก

inv = {}
add_stock(inv, "apple", 3)
add_stock(inv, "apple", 3)
print(inv)
```
