# 🔁 Practice Review — ข้อ 16: เมนูสั่งอาหาร

**Difficulty:** 🔴 Challenge

---

## โจทย์

เมนูเป็น dict ราคา และรายการสั่งเป็น list

**เงื่อนไข:**

- `menu = {"rice": 40, "soup": 30, "tea": 20}`
- `order = ["rice", "tea", "soup"]`
- สร้าง `bill(menu, order)` คืนยอดรวม
- พิมพ์ยอด

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
90
```


---

## 💡 Hint

วน order แล้วบวกจาก menu

---

## Starter Code

```python
menu = {"rice": 40, "soup": 30, "tea": 20}
order = ["rice", "tea", "soup"]

def bill(menu, order):
    # รวมราคา

print(bill(menu, order))
```
