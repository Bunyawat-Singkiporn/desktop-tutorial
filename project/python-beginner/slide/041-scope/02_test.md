# 🔭 Practice Scope — Question 1: Predict Output

**Difficulty:** 🟢 Easy

---

## โจทย์

อ่านโค้ดด้านล่างแล้วทำนาย output โดยไม่ต้องรัน
แล้วเขียนโค้ดที่ถูกต้องเพื่อยืนยัน

```python
x = 10

def change():
    x = 99
    print("Inside:", x)

change()
print("Outside:", x)
```

**Output ที่ถูกต้อง:**
```
Inside: 99
Outside: 10
```

---

## 💡 คำถาม

ทำไม `x` ภายนอกยังเป็น `10` แม้ว่า `change()` จะกำหนด `x = 99`?

---

## Starter Code

```python
x = 10

def change():
    x = 99
    print("Inside:", x)

change()
print("Outside:", x)
# เพิ่ม comment อธิบายว่าทำไม x ภายนอกไม่เปลี่ยน
```
