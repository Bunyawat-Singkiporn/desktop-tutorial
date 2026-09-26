# ↩️ Return Values — ข้อ 10: clamp คะแนน 0-100

**Difficulty:** 🟡 Medium

---

## โจทย์

บังคับคะแนนให้อยู่ระหว่าง 0 ถึง 100

**เงื่อนไข:**

- สร้าง `clamp(score)` ถ้า < 0 คืน 0 ถ้า > 100 คืน 100 ไม่งั้นคืน score
- พิมพ์ผลของ `-5` `40` `150`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)

## Output

3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
0
40
100
```


---

## 💡 Hint

ใช้ if/elif/else คืนค่า

---

## Starter Code

```python
def clamp(score):
    # return
    # เขียนโค้ดตรงนี้

print(clamp(-5))
print(clamp(40))
print(clamp(150))
```
