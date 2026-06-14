# 🔥 Practice Even / Odd — Question 4: Score Bonus

**Difficulty:** 🔴 Hard

---

## โจทย์

รับคะแนน **2 วิชา** แล้วคำนวณผลรวม จากนั้น:

**เงื่อนไขที่ 1 — ตรวจ Bonus:**

| เงื่อนไข | Output |
|----------|--------|
| ผลรวมเป็นเลข**คู่** | `Bonus! Total: [X + 10]` |
| ผลรวมเป็นเลข**คี่** | `No Bonus. Total: [X]` |

**เงื่อนไขที่ 2 — ตรวจ Pass/Fail (จากผลรวมก่อนบวก Bonus):**

| เงื่อนไข | Output |
|----------|--------|
| ผลรวม >= 100 | `Pass` |
| ผลรวม < 100 | `Fail` |

---

## ตัวอย่าง

**Input:**
```
55
45
```

**Output:**
```
Bonus! Total: 110
Pass
```

> 55 + 45 = 100 (เลขคู่) → Bonus +10 = 110 | 100 >= 100 → Pass

**Input:**
```
40
31
```

**Output:**
```
No Bonus. Total: 71
Fail
```

> 40 + 31 = 71 (เลขคี่) → ไม่ได้ Bonus | 71 < 100 → Fail

---

## 💡 Hint

- ใช้ `%` ตรวจเลขคู่/คี่ของผลรวม
- ใช้ `if/else` แยกกัน **2 บล็อค** (ตรวจ bonus ก่อน แล้วค่อยตรวจ pass/fail)
- ทั้งสองบล็อคใช้ผลรวม **ก่อน** บวก bonus

---

## Starter Code

```python
a = int(input())
b = int(input())

total = a + b

# Write your code here
```

- ตรวจ `% 15 == 0` ก่อน (หรือ `% 3 == 0 and % 5 == 0`)
- ต้องเรียง `if` จากเงื่อนไขที่แคบที่สุดก่อน

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    # Write your code here
```
