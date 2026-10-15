♪ Code Readability

---

♪ What's a good code? !

A good code isn't only possible but easily read. *

---

♪ Named it to mean ♪

```python
# ❌ อ่านไม่รู้เรื่อง
x = 75
y = x >= 50

# ✅ อ่านเข้าใจทันที
score = 75
is_passed = score >= 50
```---

# Indientation right

```python
# ❌ indent ผิด
def greet():
print("Hello")     # ← ควรเว้น 4 ช่อง

# ✅ ถูกต้อง
def greet():
    print("Hello")
```---

#### Use only necessary applications

```python
# ❌ comment ทุกบรรทัด (รก)
x = 10       # กำหนด x เป็น 10
y = 20       # กำหนด y เป็น 20
z = x + y    # บวก x กับ y

# ✅ comment เฉพาะจุดที่อธิบายเหตุผล
DISCOUNT_RATE = 0.1   # 10% discount for all items
price = 200
final_price = price * (1 - DISCOUNT_RATE)
```---

## Use f-sting instead of stringing

```python
# ❌ อ่านยาก
print("Name: " + name + ", Age: " + str(age))

# ✅ อ่านง่าย
print(f"Name: {name}, Age: {age}")
```---

# Funtion instead of code #

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
```---

# Five clean code mains

One, name to mean it.
Two things, always make it right.
3.
Four. Use f-stinging.
Five division functions for each event.
