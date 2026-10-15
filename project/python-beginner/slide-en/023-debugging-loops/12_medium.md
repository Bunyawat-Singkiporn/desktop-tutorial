♪ debugging-loops ^QC12: Edit break too fast

difficulty:* ^Medium

---

♪ Task

Print Q [ "Wait," "Wait," "Serve," "Wait"]

---

♪ Input

No.

♪ Output

Wait wait, Serve

---

## Example

♪ Output:*```text
Wait
Wait
Serve
```---

♪ Hint

Print first, then break

---

♪ Starter Code```python
queue = ["Wait", "Wait", "Serve", "Wait"]
for item in queue:
    if item == "Serve":
        break
    print(item)
```
