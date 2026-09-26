# 🔭 Scope — ข้อ 6: ภาษีจากเรทนอก

**Difficulty:** 🟡 Medium

---

## โจทย์

อัตราภาษีเก็บเป็น global

**เงื่อนไข:**

- `TAX = 0.07`
- `with_tax(amount)` คืน amount * (1 + TAX)
- พิมพ์ผลของ `100` ทศนิยม 2 ตำแหน่ง

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
107.00
```


---

## 💡 Hint

อ่าน TAX ได้โดยไม่ต้อง global ถ้าไม่แก้ค่า

---

## Starter Code

```python
TAX = 0.07

def with_tax(amount):
    # ใช้ TAX

print(f"{with_tax(100):.2f}")
```
