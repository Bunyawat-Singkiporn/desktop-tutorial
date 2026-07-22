# 💾 Dictionary Practice — ฝึกใช้ Dictionary

---

## ทบทวน Dictionary ที่เรียนมา

| ทักษะ | ตัวอย่าง |
|-------|---------|
| สร้าง | `d = {"a": 1, "b": 2}` |
| เข้าถึง | `d["a"]` → `1` |
| เพิ่ม/แก้ | `d["c"] = 3` |
| อัปเดต | `d.update({"a": 10})` |
| ลบ | `del d["b"]` |
| loop | `for k, v in d.items():` |

---

## Pattern ที่พบบ่อย — นับความถี่

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
# {'cat': 3, 'dog': 2, 'bird': 1}
```

---

## Pattern — ตรวจสอบคำตอบ

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
user_answer = input("q1: ")

if user_answer == answers["q1"]:
    print("Correct!")
else:
    print("Wrong!")
```

---

## ตัวอย่างโปรแกรม — ราคาสินค้า

```python
prices = {"apple": 15, "banana": 8, "mango": 25}
total = 0

for item, price in prices.items():
    print(f"{item}: {price} บาท")
    total += price

print(f"รวม: {total} บาท")
```
