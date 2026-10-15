# Final Review #

difficulty:

---

♪ Task

IDt of list scores, name and sum

== sync, corrected by elderman == *

[10, 20], "B": [30, 5] ♫
- Type: 30) and ^B:35 ▪

---

♪ Input

None

♪ Output

Two lines.

---

## Example

♪ Output:*

```text
A: 30
B: 35
```


---

## 💡 Hint

dict of lists

---

## Starter Code

```python
room = {"A": [10, 20], "B": [30, 5]}
for name, scores in room.items():
    print(f"{name}: {sum(scores)}")
```
