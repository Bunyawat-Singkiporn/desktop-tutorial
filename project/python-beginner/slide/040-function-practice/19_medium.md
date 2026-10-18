# 🧩 Function Practice — ข้อ 19: สั่งชานมไข่มุก

**Difficulty:** 🟡 Medium

---

## โจทย์

ร้านชานมมีราคาแก้วพื้นฐาน และท็อปปิ้งชิ้นละ 10 บาท
พนักงานอยากให้ระบบช่วยคิดราคาสุดท้ายจากราคาแก้วกับจำนวนท็อปปิ้ง

แยกหน้าที่เป็นสองฟังก์ชัน แล้วประกอบกัน

**เงื่อนไข:**

- `topping_cost(count)` คืน `count * 10`
- `final_price(base, count)` คืนราคาแก้วรวมท็อปปิ้ง โดยเรียกใช้ `topping_cost`
- รับราคาแก้วและจำนวนท็อปปิ้ง แล้วพิมพ์ราคาสุดท้าย

## ตัวอย่าง

**Input:**

```text
45
2
```

**Output:**

```text
65
```

---

## 💡 Hint

ฟังก์ชันหนึ่งเรียกอีกฟังก์ชันได้ — อย่าคำนวณท็อปปิ้งซ้ำใน `final_price`

---

## Starter Code

```python
def topping_cost(count):
    # เขียนโค้ดตรงนี้

def final_price(base, count):
    # เขียนโค้ดตรงนี้

base = int(input())
count = int(input())
print(final_price(base, count))
```
