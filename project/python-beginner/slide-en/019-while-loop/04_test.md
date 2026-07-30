# 🔑 Practice: while Loop — Question 3: Password Checker

**Difficulty:** 🟡 Medium

---

## Problem

Repeat password until typed correctly (code is `"python123"`)

**Input/Output:**
```
Input: hello
Wrong password! Try again.
Input: test
Wrong password! Try again.
Input: python123
Access granted!
```

---

## 💡 Hint

- Use `while password != "python123":`
- Receive input at the beginning of the round and repeat it each round.

---

## Starter Code

```python
password = input()

while password != "python123":
    print("Wrong password! Try again.")
    # Get new input

print("Access granted!")
```
