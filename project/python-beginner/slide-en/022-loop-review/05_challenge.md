# 🔥 Practice: Loop Review — Question 4: FizzBuzz

**Difficulty:** 🔴 Hard

---

## Problem

Take n and display the numbers 1 through n according to the rule:

|condition|show|
|----------|------|
|Divisible by 15.| `FizzBuzz` |
|Divisible by 3.| `Fizz` |
|Divisible by 5| `Buzz` |
|other|that number|

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

- Check `% 15` first (a number that is divisible by both 3 and 5).
- Then check `% 3`, `% 5` respectively.

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
