# Final Review QC5: basket project

difficulty:

---

♪ Task

A basket is a list of prices and a coupon is a dict.

== sync, corrected by elderman == *

- What do you mean? ▪
- ^coupon = { "off": 20}
- Plus the price is broken.

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
130
```---

¶ Hint ¶

Mix list with dict

---

♪ Starter Code

```python
prices = [100, 50]
coupon = {"off": 20}
print(sum(prices) - coupon["off"])
```
