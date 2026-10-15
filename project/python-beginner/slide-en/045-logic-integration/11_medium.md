# Logic Integration QC11: including the cost of dict

difficulty:* ^Medium

---

♪ Task

Order food from the dict menu

== sync, corrected by elderman == *

- ^menu = {a ": 40, "b": 25} ▪
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
105
```---

¶ Hint ¶

Round order pulling price

---

♪ Starter Code

```python
menu = {"a": 40, "b": 25}
order = ["a", "b", "a"]
total = 0
for item in order:
    total += menu[item]
print(total)
```
