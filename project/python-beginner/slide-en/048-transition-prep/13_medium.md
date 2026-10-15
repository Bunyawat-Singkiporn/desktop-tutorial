# ^ Transition Prep □ Q13: Mix dict+loupe

difficulty:* ^Medium

---

♪ Task

^Progress = {" waves ": 1, "lops": 1, "funcs": 1}

---

♪ Input

None

♪ Output

Three lines.

---

## Example

♪ Output:*

```text
vars: 1
loops: 1
funcs: 1
```---

¶ Hint ¶

Use .items)

---

♪ Starter Code

```python
progress = {"vars": 1, "loops": 1, "funcs": 1}
for k, v in progress.items():
    print(f"{k}: {v}")
```
