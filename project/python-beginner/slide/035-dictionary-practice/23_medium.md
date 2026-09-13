# Practice Dictionary — Question 22: สั่งของ 2 ชิ้น

**Difficulty:** 🟡 Medium

---

## โจทย์

รับชื่อสินค้า 2 ชิ้นจากร้าน แล้วคิดราคารวม

```python
prices = {"pen": 10, "book": 40, "eraser": 5, "ruler": 15}
```

**ตัวอย่าง Session:**
```
Item 1: pen
Item 2: book
Total: 50 baht
```

ถ้าชิ้นไหนไม่มี → ไม่บวกราคาชิ้นนั้น (ข้ามได้)

---

## Starter Code

```python
prices = {"pen": 10, "book": 40, "eraser": 5, "ruler": 15}
total = 0

for i in range(2):
    item = input(f"Item {i+1}: ")
    # Write your code here

print(f"Total: {total} baht")
```
