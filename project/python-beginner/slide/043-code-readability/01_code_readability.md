# ✨ Code Readability — โค้ดที่อ่านง่าย

---

## โค้ดที่ดีคืออะไร?

โค้ดที่ดีไม่ใช่แค่ **รันได้** แต่ต้อง **อ่านเข้าใจได้ง่าย**

---

## ตั้งชื่อให้สื่อความหมาย

```python
# ❌ อ่านไม่รู้เรื่อง
x = 75
y = x >= 50

# ✅ อ่านเข้าใจทันที
score = 75
is_passed = score >= 50
```

---

## Indentation ให้ถูกต้อง

```python
# ❌ indent ผิด
def greet():
print("Hello")     # ← ควรเว้น 4 ช่อง

# ✅ ถูกต้อง
def greet():
    print("Hello")
```

---

## ใช้ Comment เฉพาะที่จำเป็น

```python
# ❌ comment ทุกบรรทัด (รก)
x = 10       # กำหนด x เป็น 10
y = 20       # กำหนด y เป็น 20
z = x + y    # บวก x กับ y

# ✅ comment เฉพาะจุดที่อธิบายเหตุผล
DISCOUNT_RATE = 0.1   # 10% discount for all items
price = 200
final_price = price * (1 - DISCOUNT_RATE)
```

---

## ใช้ f-string แทนการต่อ string

```python
# ❌ อ่านยาก
print("Name: " + name + ", Age: " + str(age))

# ✅ อ่านง่าย
print(f"Name: {name}, Age: {age}")
```

---

## แบ่ง Function แทนโค้ดยาว

```python
# ❌ โค้ดยาวอัดแน่น
n = int(input())
t = 0
for i in range(n):
    t += i
print(t)

# ✅ แบ่งชัดเจน
def get_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

n = int(input())
print(get_sum(n))
```

---

## หลัก Clean Code 5 ข้อ

1. ตั้งชื่อให้สื่อความหมาย
2. Indent ให้ถูกต้องเสมอ
3. Comment เฉพาะจุดที่ซับซ้อน
4. ใช้ f-string
5. แบ่ง function สำหรับงานแต่ละอย่าง
