# Code Readability #

difficulty:* ^Medium

---

♪ Task

Calculate change with a line of complements. Why?

== sync, corrected by elderman == *

- Get the price and pay.
- Print {0}:<paid-price)

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
70
100
```

**Output:**

```text
Change: 30
```---

¶ Hint ¶

Comment explains why, not repeat the code.

---

♪ Starter Code

```python
price = int(input())
paid = int(input())
# คำนวณเงินทอนให้ลูกค้า
change = paid - price
print(f"Change: {change}")
```
