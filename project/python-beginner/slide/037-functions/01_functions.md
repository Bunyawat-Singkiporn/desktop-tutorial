# ⚙️ Functions — ฟังก์ชัน

---

## Function คืออะไร?

Function คือ **ชุดคำสั่งที่ตั้งชื่อไว้** เรียกใช้ซ้ำได้

---

## ทำไมต้องใช้ Function?

โค้ดที่ไม่มี function:
```python
print("Hello Alice")
print("Hello Bob")
print("Hello Charlie")
```

โค้ดที่ใช้ function:
```python
def greet():
    print("Hello!")

greet()
greet()
greet()
```

> เขียนครั้งเดียว ใช้ได้หลายครั้ง

---

## การสร้าง Function (Define)

```python
def function_name():
    # คำสั่งข้างใน
    print("Hello!")
```

- `def` = คำสงวน บอกว่ากำลังสร้าง function
- `function_name` = ชื่อ function
- `:` = จบบรรทัด def
- คำสั่งข้างใน **ต้อง indent** 4 ช่อง

---

## การเรียกใช้ Function (Call)

```python
def greet():
    print("Hello!")
    print("Nice to meet you!")

greet()   # เรียกใช้ครั้งแรก
greet()   # เรียกใช้ครั้งที่สอง
```

**Output:**
```
Hello!
Nice to meet you!
Hello!
Nice to meet you!
```

---

## ลำดับสำคัญ

```
1. Define (สร้าง) ก่อน
2. Call (เรียก) ทีหลัง
```

```python
# ❌ ผิด — เรียกก่อนสร้าง
greet()
def greet():
    print("Hello!")

# ✅ ถูก — สร้างก่อนเรียก
def greet():
    print("Hello!")
greet()
```
