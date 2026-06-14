# 🔥 Practice Even / Odd — Question 4: Fizz Buzz Lite

**Difficulty:** 🔴 Hard

---

## โจทย์

รับตัวเลข N แล้ววนแสดงเลข **1 ถึง N** โดย:

| เงื่อนไข | Output |
|----------|--------|
| หารด้วย 3 **และ** 5 ลงตัว | `FizzBuzz` |
| หารด้วย 3 ลงตัว (เท่านั้น) | `Fizz` |
| หารด้วย 5 ลงตัว (เท่านั้น) | `Buzz` |
| อื่น ๆ | แสดงตัวเลขนั้น |

> ผสมความรู้: for loop + even/odd (%) + elif

---

## ตัวอย่าง

**Input:**
```
15
```

**Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

## 💡 Hint

- ตรวจ `% 15 == 0` ก่อน (หรือ `% 3 == 0 and % 5 == 0`)
- ต้องเรียง `if` จากเงื่อนไขที่แคบที่สุดก่อน

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    # Write your code here
```
