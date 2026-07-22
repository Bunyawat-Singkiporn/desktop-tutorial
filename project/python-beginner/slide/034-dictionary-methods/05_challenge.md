# 🔥 Practice Dictionary Methods — Question 4: Contact Editor

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้าง contact editor ที่ทำได้ 3 คำสั่ง: `show`, `update`, `delete`

```python
contact = {
    "name": "Alice",
    "phone": "081-111-1111",
    "city": "Bangkok"
}
```

| คำสั่ง | ผล |
|--------|-----|
| `show` | แสดงทุก key-value |
| `update` | รับ key และค่าใหม่แล้วอัปเดต |
| `delete` | รับ key แล้วลบออก |
| `exit` | จบโปรแกรม |

**ตัวอย่าง Session:**
```
Command: show
name: Alice
phone: 081-111-1111
city: Bangkok
Command: update
Key: city
Value: Chiang Mai
Command: delete
Key: phone
Command: show
name: Alice
city: Chiang Mai
Command: exit
```

---

## Starter Code

```python
contact = {
    "name": "Alice",
    "phone": "081-111-1111",
    "city": "Bangkok"
}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
