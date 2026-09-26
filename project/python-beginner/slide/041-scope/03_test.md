# 🔭 Scope — ข้อ 3: local ทับชื่อ

**Difficulty:** 🟢 Easy

---

## โจทย์

ตัวแปรชื่อเดียวกันคนละที่

**เงื่อนไข:**

- นอกฟังก์ชัน `x = 100`
- ใน `demo()` ตั้ง `x = 50` แล้วพิมพ์ `Inside: 50`
- หลังเรียกฟังก์ชันพิมพ์ `Outside: 100`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

2 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Inside: 50
Outside: 100
```


---

## Starter Code

```python
x = 100

def demo():
    # local x

demo()
print(f"Outside: {x}")
```
