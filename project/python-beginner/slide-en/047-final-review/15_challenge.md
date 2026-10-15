# Final Review #

difficulty:

---

♪ Task

Take choice 1 = plus 2 = multiply and take a, type b The result.

== sync, corrected by elderman == *

- There are functions.

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
2
3
4
```

**Output:**

```text
12
```---

¶ Hint ¶

Select function on menu

---

♪ Starter Code

```python
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

op = int(input())
a = int(input())
b = int(input())
if op == 1:
    print(add(a, b))
else:
    print(mul(a, b))
```
