# 🔁 Loop Review — Review every Loop.

---

## Summary of loops learned

| Loop |Use when|example|
|------|---------|---------|
| `for range()` |Know the exact number of turns|Count 1–10|
| `for list` |Cycle through members on the list|Show list|
| `while` |Cycle until the condition is False.|Receive duplicate input|
| `nested` |loop nested loop|create pattern, table|
| `break` |Stopped midway.|Find the desired value|
| `continue` |skip some rounds|Filter data|

---

## Combined Example 1: Find Sum + Average

```python
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
```

```
Total: 438
Average: 87.6
```

---

## Combined example 2: Repeat input until 0 is printed.

```python
total = 0
count = 0

while True:
    number = int(input())
    if number == 0:
        break
    total += number
    count += 1

print(f"Count: {count}, Total: {total}")
```

---

## Example included 3: Pattern according to size

```python
n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()
```

Input: `4`
```
*
**
***
****
```

---

## How to choose a loop?

```
Do you know the number of rounds?
YES → for range() or for list
 NO  → while
Have to stop halfway?  → Use break
Have to skip some rounds?   → Use continue
```
