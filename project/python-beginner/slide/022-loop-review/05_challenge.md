# 🔥 Practice: Loop Review — Question 4: FizzBuzz

**Difficulty:** 🔴 Hard

---

## โจทย์

รับ n แล้วแสดงตัวเลข 1 ถึง n ตามกฎ:

| เงื่อนไข | แสดง |
|----------|------|
| หารด้วย 15 ลงตัว | `FizzBuzz` |
| หารด้วย 3 ลงตัว | `Fizz` |
| หารด้วย 5 ลงตัว | `Buzz` |
| อื่นๆ | ตัวเลขนั้น |

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

- ตรวจ `% 15` ก่อน (เลขที่หารได้ทั้ง 3 และ 5)
- แล้วตรวจ `% 3`, `% 5` ตามลำดับ

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
