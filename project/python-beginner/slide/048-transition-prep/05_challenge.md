# 🚀 Transition Prep — ข้อ 5: มินิโปรเจกต์ร้าน

**Difficulty:** 🔴 Challenge

---

## โจทย์

ร้านมีเมนู dict และออเดอร์ list

**เงื่อนไข:**

- `menu = {"bun": 25, "milk": 20}`
- `order = ["bun", "milk", "bun"]`
- พิมพ์ยอดรวม

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
70
```


---

## 💡 Hint

วนออเดอร์บวกราคา

---

## Starter Code

```python
menu = {"bun": 25, "milk": 20}
order = ["bun", "milk", "bun"]
total = 0
for item in order:
    total += menu[item]
print(total)
```
