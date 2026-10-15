# 🐛 debugging-loops — ข้อ 13: แก้เฉลี่ยอุณหภูมิ

**Difficulty:** 🟡 Medium

---

## โจทย์

อุณหภูมิ `[28, 30, 32]` ต้องได้ `Average: 30.0`
ย้ายการหารออกมานอกลูป

---

## ตัวอย่าง

**Output:**

```text
Average: 30.0
```


---

## 💡 Hint

รวมให้ครบก่อน แล้วค่อยหารครั้งเดียว

---

## Starter Code

```python
temps = [28, 30, 32]
total = 0
for t in temps:
    total = total + t
    average = total / len(temps)
print(f"Average: {average:.1f}")
```
