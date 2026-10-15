♪ Transition Prep QC: mini Project

difficulty:

---

♪ Task

The store has dict and order list.

== sync, corrected by elderman == *

- ^menu = { "bun": 25, "milk": 20}
- What? ▪
- Total printing.

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
70
```---

¶ Hint ¶

Auror plus price.

---

♪ Starter Code

```python
menu = {"bun": 25, "milk": 20}
order = ["bun", "milk", "bun"]
total = 0
for item in order:
    total += menu[item]
print(total)
```
