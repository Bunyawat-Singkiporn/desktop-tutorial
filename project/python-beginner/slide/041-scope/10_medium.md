# 🔭 Scope — ข้อ 10: สวิตช์ไฟ

**Difficulty:** 🟡 Medium

---

## โจทย์

สถานะไฟเป็น global bool

**เงื่อนไข:**

- `is_on = False`
- `turn_on()` ตั้ง is_on เป็น True ด้วย global
- เรียก turn_on แล้วพิมพ์ is_on

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
True
```


---

## 💡 Hint

แก้ bool ด้วย global

---

## Starter Code

```python
is_on = False

def turn_on():
    # global

turn_on()
print(is_on)
```
