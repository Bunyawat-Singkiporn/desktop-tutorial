# 🏷️ Naming Rules — กฎการตั้งชื่อ Variable

---

## ทำไมชื่อ Variable ถึงสำคัญ?

```python
# ❌ อ่านไม่รู้เรื่อง
x = 100
y = 50
print(x - y)
```

```python
# ✅ เข้าใจทันที
price = 100
discount = 50
print(price - discount)
```

> โค้ดทั้งสองทำงานเหมือนกัน แต่ชื่อที่ดีทำให้อ่านเข้าใจทันที!

---

## กฎที่ต้องรู้

| กฎ | ✅ ถูก | ❌ ผิด |
|----|--------|--------|
| ใช้ได้: ตัวอักษร, ตัวเลข, `_` | `player1`, `my_score` | `player 1`, `my-score` |
| ห้ามขึ้นต้นด้วยตัวเลข | `score1` | `1score` |
| ห้ามมีช่องว่าง | `first_name` | `first name` |
| ใช้ตัวพิมพ์เล็กทั้งหมด | `my_name` | `MyName`, `MY_NAME` |
| ชื่อต้องสื่อความหมาย | `total_price` | `tp`, `x`, `aaa` |

---

## Snake Case คืออะไร?

**snake_case** คือการเขียนชื่อหลายคำโดยใช้ `_` คั่น (เหมือนงูเลื้อย)

```python
# snake_case ✅ (Python style)
first_name = "Alice"
total_price = 100
player_score = 0
is_game_over = False

# camelCase ❌ (ใช้ใน JavaScript ไม่ใช่ Python)
firstName = "Alice"
totalPrice = 100
```

---

## ตัวอย่างชื่อที่ดี vs แย่

| ❌ แย่ | ✅ ดี | เหตุผล |
|--------|-------|--------|
| `n` | `name` | สั้นเกินไป |
| `p` | `price` | ไม่สื่อความหมาย |
| `s1` | `student_name` | ตัวเลขไม่บอกความหมาย |
| `MyAge` | `my_age` | ควรใช้ snake_case |
| `TOTAL` | `total` | ตัวใหญ่ใช้กับ constant เท่านั้น |
| `data1` | `product_price` | ควรบอกว่าเก็บอะไร |

---

## ชื่อ Variable ที่ห้ามใช้ (Keywords)

Python มีคำสงวน (Keywords) ที่ห้ามใช้เป็นชื่อ variable:

```python
# ❌ ห้ามใช้:
if = 5       # SyntaxError
for = 10     # SyntaxError
print = "hi" # จะทำให้ print() เสียหาย!
```

| Keywords ที่พบบ่อย |
|------------------|
| `if`, `else`, `for`, `while` |
| `print`, `input`, `True`, `False` |

---

## ตัวอย่างโปรแกรมที่ตั้งชื่อดี

```python
# ข้อมูลสินค้า
product_name = "T-Shirt"
original_price = 500
discount_amount = 100
final_price = original_price - discount_amount

print("Product:", product_name)
print("Price:", final_price)
```

ผลลัพธ์:
```
Product: T-Shirt
Price: 400
```
