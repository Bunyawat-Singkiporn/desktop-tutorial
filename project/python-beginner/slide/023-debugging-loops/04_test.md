# 🐛 debugging-loops — ข้อ 4: แก้ indent ใบเสร็จ

**Difficulty:** 🟢 Easy

---

## โจทย์

ต้องการพิมพ์รายการสินค้า 3 ชิ้นในลูป แต่ `print` อยู่นอกลูป
จัด indent ให้พิมพ์ครบ

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

Item 1 ถึง Item 3

---

## ตัวอย่าง

**Output:**

```text
Item 1
Item 2
Item 3
```


---

## 💡 Hint

คำสั่งที่ต้องทำทุกรอบต้องอยู่ในลูป

---

## Starter Code

```python
for i in range(1, 4):
    pass
print(f"Item {i}")  # ← จัด indent / ลบ pass
```
