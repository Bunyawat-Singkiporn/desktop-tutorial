# 🔥 Practice if/else — Question 4: Ticket Price

**Difficulty:** 🔴 Hard

---

## Problem

Get the age and day (weekday or weekend) and calculate the ticket price.

**Condition 1 — Age verification:**

|condition|Basic price|
|----------|-------------|
|Age >= 60|50 baht (seniors)|
|Age < 60|100 baht (normal)|

**Condition 2 — Check the date:**

|condition|Increase the price|
|----------|-----------|
| `weekend` |+20 baht|
| `weekday` |no increase|

> Get age first line. Get date (`weekday` or `weekend`) second line.

---

## example

**Input:**
```
65
weekend
```

**Output:**
```
70
```

> Seniors 50 + weekend 20 = 70

---

## 💡 Hint

- Use two separate sets of `if/else`.
- First set of age verification → Set price
- The second set checks the date → increases the price.

---

## Starter Code

```python
age = int(input())
day = input()

# Write your code here
```
