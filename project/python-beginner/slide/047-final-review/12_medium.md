# 🏁 Final Review — ข้อ 12: สองฟังก์ชันประกอบ

**Difficulty:** 🟡 Medium

---

## โจทย์

`net(price)` คืน price หลังหัก 10 และ `label(n)` คืนสตริง `Net: <n>`

**เงื่อนไข:**

- พิมพ์ `label(net(100))`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Net: 90
```


---

## 💡 Hint

ประกอบ return

---

## Starter Code

```python
def net(price):
    return price - 10

def label(n):
    return f"Net: {n}"

print(label(net(100)))
```
