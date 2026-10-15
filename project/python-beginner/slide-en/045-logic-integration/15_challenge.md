# Logic Integration • Q15: Decent basket

difficulty:

---

♪ Task

That's a total of 200 and 20.

== sync, corrected by elderman == *

- ^ixes = [80, 70, 60] ▪
- A total discount.
- Type:

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
Pay: 190
```---

¶ Hint ¶

Let's put it back together.

---

♪ Starter Code

```python
prices = [80, 70, 60]
total = sum(prices)
if total >= 200:
    total = total - 20
print(f"Pay: {total}")
```
