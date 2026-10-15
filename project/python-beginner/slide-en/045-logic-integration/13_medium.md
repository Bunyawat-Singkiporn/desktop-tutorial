# Logic Integration ^Q13:

difficulty:* ^Medium

---

♪ Task

Count & pass and fall

== sync, corrected by elderman == *

[40, 60, 55, 30, 80]
- Print:

---

♪ Input

None

♪ Output

Two lines.

---

## Example

♪ Output:*

```text
Pass: 3
Fail: 2
```---

¶ Hint ¶

Two unknowns.

---

♪ Starter Code

```python
scores = [40, 60, 55, 30, 80]
passed = 0
failed = 0
for s in scores:
    # นับ
print(f"Pass: {passed}")
print(f"Fail: {failed}")
```
