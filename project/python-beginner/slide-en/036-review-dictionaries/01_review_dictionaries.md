# 🔄 Review Dictionaries — ทบทวน Dictionary

---

## สรุปทุกคำสั่ง

```python
# สร้าง
student = {"name": "Alice", "age": 15, "score": 90}

# เข้าถึง
print(student["name"])        # Alice

# เพิ่ม / แก้ไข
student["grade"] = "A"        # เพิ่ม key ใหม่
student["age"] = 16           # แก้ไขค่าเดิม

# อัปเดตหลายค่า
student.update({"score": 95, "age": 17})

# ลบ
del student["grade"]

# Loop ทั้งหมด
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## ตรวจสอบก่อนเข้าถึง

```python
# แนะนำ: ตรวจก่อนเสมอ
if "score" in student:
    print(student["score"])
else:
    print("No score yet")
```

---

## Pattern รวม Dictionary กับ Loop

```python
scores = {"Alice": 88, "Bob": 72, "Charlie": 95}
highest = ""
max_score = 0

for name, score in scores.items():
    if score > max_score:
        max_score = score
        highest = name

print(f"Top: {highest} ({max_score})")
```

---

## Checklist ก่อนสอบ

- [ ] สร้าง dict ได้
- [ ] เข้าถึงค่าด้วย key ได้
- [ ] เพิ่ม / แก้ไข / ลบ key ได้
- [ ] ใช้ `.update()` ได้
- [ ] loop ด้วย `.items()` ได้
- [ ] ตรวจสอบ key ด้วย `in` ได้
