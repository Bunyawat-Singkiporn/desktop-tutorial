# 🔥 Practice Even / Odd — Question 4: Score Bonus

**Difficulty:** 🔴 Hard

---

## Problem

Get scores for **2 subjects** and calculate the total, then:

**Condition 1 — Check Bonus:**

|condition| Output |
|----------|--------|
|The sum is an **even** number.| `Bonus! Total: [X + 10]` |
|The sum is an **odd** number.| `No Bonus. Total: [X]` |

**Condition 2 — Check Pass/Fail (from the total before adding Bonus):**

|condition| Output |
|----------|--------|
|Sum >= 100| `Pass` |
|Sum < 100| `Fail` |

---

## example

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

> 55 + 45 = 100 (Even number) → Bonus +10 = 110 | 100 >= 100 → Pass

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

> 40 + 31 = 71 (odd number) → no bonus | 71 < 100 → Fail

---

## 💡 Hint

- Use `%` to check the even/odd numbers of the sum.
- Use `if/else` in **2 separate blocks** (check bonus first, then check pass/fail)
- Both blocks use the sum **before** plus bonus.

---

## Starter Code

```python
a = int(input())
b = int(input())

total = a + b

# Write your code here
```

- Check `% 15 == 0` first (or `% 3 == 0 and % 5 == 0`).
- `if` must be sorted from the narrowest condition first.

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    # Write your code here
```
