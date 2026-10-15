# ^Pactice Review ^Q15:

difficulty:

---

♪ Task

The application list may be repeated. Leave a unique name.

== sync, corrected by elderman == *

"C," "A," "B," "A." ▪
- New list By adding only unknown names.
- Print output

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
['A', 'B', 'C']
```---

¶ Hint ¶

Use in with list

---

♪ Starter Code

```python
raw = ["C", "A", "B", "A"]
team = []
for name in raw:
    # เพิ่มถ้ายังไม่มี
team.sort()
print(team)
```
