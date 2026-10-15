# Final Review QC10: Count in dict

difficulty:* ^Medium

---

♪ Task

Count the letters in list ^letters = ["a," "b," "a," "c," "a"]] and then type the number ^a]

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
3
```---

¶ Hint ¶

A frequency count.

---

♪ Starter Code

```python
letters = ["a", "b", "a", "c", "a"]
freq = {}
for ch in letters:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq["a"])
```
