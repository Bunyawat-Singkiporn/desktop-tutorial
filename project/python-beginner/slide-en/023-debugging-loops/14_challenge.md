# d d d d d d d d d d d d d d d d d d d d

difficulty:

---

♪ Task

Get menu names one line at a time
Print the actual menu (not including end) and then end with ^Count: > Number
The code starts printing end and counting the end . . . . correct the condition.

---

♪ Input

Menu name by line ends with end

♪ Output

Menu list followed by Count

---

## Example

**Input:*```text
Pad Thai
Green Curry
end
```

**Output:**

```text
Pad Thai
Green Curry
Count: 2
```---

♪ Hint

Check before print and before counting

---

♪ Starter Code```python
count = 0
while True:
    menu = input()
    print(menu)
    count = count + 1
    if menu == "end":
        break
print(f"Count: {count}")
```
