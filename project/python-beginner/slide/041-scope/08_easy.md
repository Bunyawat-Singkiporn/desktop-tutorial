# 🔭 Scope — ข้อ 8: นับด้วย global

**Difficulty:** 🟢 Easy

---

## โจทย์

นับครั้งที่กดปุ่ม

**เงื่อนไข:**

- มี `count = 0` นอกฟังก์ชัน
- `add_one()` ใช้ `global count` แล้ว `count += 1`
- เรียก 2 ครั้ง แล้วพิมพ์ count

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
2
```


---

## Starter Code

```python
count = 0

def add_one():
    # ใช้ global

add_one()
add_one()
print(count)
```
