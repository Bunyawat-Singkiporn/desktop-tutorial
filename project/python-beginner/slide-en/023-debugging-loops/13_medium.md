# d d d d d d d debugging-lops d d d d the temperature rate d

difficulty:* ^Medium

---

♪ Task

[28, 30, 32]]
Move division outside the loop.

---

♪ Input

No.

♪ Output

One line Average

---

## Example

♪ Output:*```text
Average: 30.0
```---

♪ Hint

Let's add it up first and then divide it once.

---

♪ Starter Code```python
temps = [28, 30, 32]
total = 0
for t in temps:
    total = total + t
    average = total / len(temps)
print(f"Average: {average:.1f}")
```
