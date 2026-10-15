The warehouse

difficulty:

---

♪ Task

Manage the amount of goods in dict

== sync, corrected by elderman == *

- ^ad stock^inv, name, n) add number (if not started 0)
- Start {0}

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
{'apple': 6}
```---

¶ Hint ¶

Check key before positive

---

♪ Starter Code

```python
def add_stock(inv, item, n):
    # เพิ่มสต็อก

inv = {}
add_stock(inv, "apple", 3)
add_stock(inv, "apple", 3)
print(inv)
```
