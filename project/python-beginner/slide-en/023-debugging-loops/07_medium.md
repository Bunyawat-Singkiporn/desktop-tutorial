# d d d d d d d d d d da da da da da da d d d d da da da da da da da da da da d d d d da da da da da da da da da da da da da d d d d d d d da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da d d d d d d d d d d da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da da d d d d d d

difficulty:* ^Medium

---

♪ Task

The secret code is: Guess until it's printed.
Prescription:

---

♪ Input

The numbers guess a line to the code.

♪ Output

Unlocked When you're right.

---

## Example

**Input:*```text
3
7
```

**Output:**

```text
Unlocked
```---

♪ Hint

Repeated while guessing

---

♪ Starter Code```python
secret = 7
guess = int(input())
while guess == secret:  # ← แก้เงื่อนไข
    guess = int(input())
print("Unlocked")
```
