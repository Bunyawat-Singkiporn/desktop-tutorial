# 🚀 Transition Prep — ข้อ 14: เช็กความพร้อมคอลเลกชัน

**Difficulty:** 🔴 Challenge

---

## โจทย์

สร้าง list จาก input 3 ค่า แล้วพิมพ์จำนวนสมาชิกไม่ซ้ำด้วย set

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
a
b
a
```

**Output:**

```text
2
```


---

## 💡 Hint

set ตัดซ้ำ

---

## Starter Code

```python
vals = []
for i in range(3):
    vals.append(input())
print(len(set(vals)))
```
