# 🔭 Scope — ข้อ 7: เพิ่มคะแนนทีม

**Difficulty:** 🟡 Medium

---

## โจทย์

คะแนนทีมสะสมนอกฟังก์ชัน

**เงื่อนไข:**

- `score = 0`
- `add_points(n)` ใช้ global เพิ่มคะแนน
- เรียก `add_points(3)` แล้ว `add_points(5)` พิมพ์ score

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
8
```


---

## 💡 Hint

ต้องมีบรรทัด global score

---

## Starter Code

```python
score = 0

def add_points(n):
    # global score

add_points(3)
add_points(5)
print(score)
```
