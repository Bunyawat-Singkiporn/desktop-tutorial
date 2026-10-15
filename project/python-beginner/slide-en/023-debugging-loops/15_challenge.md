# d d d d d d d d d d d d d d d d d d d d d d d d d

difficulty:

---

♪ Task

Three rows per row, ^R1: one, two, three, and ^2: 1, three,
The code starts using wrong row numbers and loops in too short.

---

♪ Input

No.

♪ Output

Two seating lines.

---

## Example

♪ Output:*```text
R1: 1 2 3 
R2: 1 2 3 
```---

♪ Hint

Rows and seats should start at 1, and the seats have three spaces.

---

♪ Starter Code```python
for row in range(2):
    print(f"R{row}:", end=" ")
    for seat in range(2):
        print(seat, end=" ")
    print()
```
